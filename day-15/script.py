def get_start_params(inp):
    mem = {}
    latest = inp.pop()
    for i, v in enumerate(inp):
        mem[v] = [i]
    return latest, mem


def main():
    start = [19,0,5,1,10,13]
    latest, mem = get_start_params(start)
    i = len(mem.values())
    while i < 30000000:
        print("Turn %03d: %s" % (i+1, latest))
        new = latest not in mem.keys()
        if new:
            mem[latest] = [i]
            latest = 0
        else:
            mem[latest].append(i)
            latest = mem[latest][-1] - mem[latest][-2]
        i += 1


if __name__ == "__main__":
    main()
