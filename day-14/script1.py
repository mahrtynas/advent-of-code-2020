import re


class Computah:
    def __init__(self):
        self.mask = ""
        self.mem = [0 for _ in range(100)]
        self.l = len(self.mem)

    def process_line(self, x):
        cmd, value = re.findall("(.+)\\s=\\s(.+)", x)[0]
        if cmd == "mask":
            self.mask = value
        else:
            address = int(re.search("\\d+", cmd)[0])
            self._write_value(address, value)

    def _write_value(self, address, value):
        # convert to bin
        masked_value = self._mask_value(value)
        try:
            self.mem[address] = masked_value
        except IndexError:
            n = address - self.l + 1
            self.mem += [0 for _ in range(n)]
            self.l = len(self.mem)
            self.mem[address] = masked_value

    def _mask_value(self, value):
        value = "%036d" % int(bin(int(value))[2:])
        m_value = "".join([x if self.mask[i] == "X" else self.mask[i] for i, x in enumerate(value)])
        return int(m_value, 2)


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    comp = Computah()
    for line in lines:
        comp.process_line(line)
    print(sum(comp.mem))


if __name__ == "__main__":
    main()
