import re


class Program:
    def __init__(self, boot_code="input.txt"):
        self.accumulator = 0
        self.position = 0
        self.commands = []
        with open(boot_code, "r") as f:
            lines = f.read().splitlines()
        for line in lines:
            self._parse_line(line)
        self.executed_commands = set()

    def run(self):
        if self._is_looping():
            self._fix_loop()

    def _parse_line(self, line):
        command, value = re.findall("^(.{3})\\s(.+)$", line)[0]
        value = int(value)
        self.commands.append({"name": command, "value": value})

    def _execute_command(self, command):
        self.executed_commands.add(self.position)
        if command["name"] == "nop":
            self.position += 1
        if command["name"] == "acc":
            self.accumulator += command["value"]
            self.position += 1
        if command["name"] == "jmp":
            self.position += command["value"]

    def _reset_values(self):
        self.accumulator = 0
        self.position = 0
        self.executed_commands = set()

    def _is_looping(self, verbose=True):
        self._reset_values()
        looping = False
        while True:
            if self.position >= len(self.commands):
                print("No loop detected. Accumulator value : %s" % self.accumulator)
                return False
            cmd = self.commands[self.position]
            self._execute_command(cmd)
            if self.position in self.executed_commands:
                if verbose:
                    print("Loop detected. Accumulator value: %s" % self.accumulator)
                return True

    def _fix_loop(self):
        for i, cmd in enumerate(self.commands):
            if cmd["name"] == "jmp":
                self.commands[i]["name"] = "nop"
                if self._is_looping(verbose=False):
                    self.commands[i]["name"] = "jmp"
                    continue
                else:
                    print("Loop was fixed by changing jmp to nop in line %s" % i)
                    return 
            if cmd["name"] == "nop":
                self.commands[i]["name"] = "jmp"
                if self._is_looping(verbose=False):
                    self.commands[i]["name"] = "nop"
                    continue
                else:
                    print("Loop was fixed by changing jmp to nop in line %s" % i)
                    return