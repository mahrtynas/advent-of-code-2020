import re
import itertools


class Computah:
    def __init__(self):
        self.mask = ""
        self.mem = {}

    def process_line(self, x):
        cmd, value = re.findall("(.+)\\s=\\s(.+)", x)[0]
        if cmd == "mask":
            self.mask = value
        else:
            address = int(re.search("\\d+", cmd)[0])
            addresses = self._get_addresses(address)
            for ad in addresses:
                self._write_value(ad, int(value))

    def _write_value(self, address, value):
        self.mem.update({address: value})

    def _mask_value(self, value):
        value = "%036d" % int(bin(value)[2:])
        m_value = "".join([x if self.mask[i] == "X" else self.mask[i] for i, x in enumerate(value)])
        return int(m_value, 2)

    def _get_addresses(self, original_address):
        bin_address = "%036d" % int(bin(int(original_address))[2:])
        x_adr = [x for x in itertools.product('01', repeat = self.mask.count("X"))]
        addresses = []
        for x in x_adr:
            vals = list(x)
            tmp_adr = [a if self.mask[i] == '0' else vals.pop() if self.mask[i] == "X" else '1' for i, a in enumerate(bin_address)]
            addresses.append(int("".join(tmp_adr), 2))
        return addresses


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    comp = Computah()
    for i, line in enumerate(lines):
        comp.process_line(line)
    print(sum(comp.mem.values()))


if __name__ == "__main__":
    main()
