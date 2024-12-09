from copy import deepcopy
def print_map(map):
    with open("2024/8/output.txt", 'w') as file:
        for line in map:
            file.write("".join(line))
            file.write("\n")


def part1():
    map = [list(line) for line in open("2024/8/input.txt").read().split("\n")]
    map_w_anti = deepcopy(map)

    nrow = len(map)
    ncol = len(map[0])
    p1 = 0

    # freqs = set()
    # for row in map:
    #     for character in row:
    #         if character != ".":
    #             freqs.add(character)

    antinodes = set()
    antinodes_chars = set()

    for ir, r in enumerate(map):
        for ic, c in enumerate(r):
            if c != ".":
                for iir, rr in enumerate(map):
                    for iic, cc in enumerate(rr):
                        if c == cc and (iir, iic) != (ir, ic):
                            ir_anti = 2*iir - ir
                            ic_anti = 2*iic - ic
                            if 0<=ir_anti<nrow and 0<=ic_anti<ncol:
                                map_w_anti[ir_anti][ic_anti] = "#"
                                antinode = (ir_anti, ic_anti)
                                if antinode not in antinodes:
                                    antinodes.add(antinode)
                                    p1 += 1
                                antinodes_chars.add((ir_anti, ic_anti, c))
                print_map(map_w_anti)
                1 == 1

    print(f"p1: {p1}")
    print(f"")

def part2():
    map = [list(line) for line in open("2024/8/input.txt").read().split("\n")]
    map_w_anti = deepcopy(map)

    nrow = len(map)
    ncol = len(map[0])
    p2 = 0

    antinodes = set()
    antinodes_chars = set()

    for ir, r in enumerate(map):
        for ic, c in enumerate(r):
            if c != ".":
                for iir, rr in enumerate(map):
                    for iic, cc in enumerate(rr):
                        if c == cc and (iir, iic) != (ir, ic):
                            dr = iir - ir
                            dc = iic - ic
                            ar = ir + dr
                            ac = ic + dc

                            while True:
                                if not(0<=ar<nrow and 0<=ac<ncol):
                                    break
                                antinode = (ar, ac)
                                if antinode not in antinodes:
                                    antinodes.add(antinode)
                                    p2 += 1
                                antinodes_chars.add((ar, ac, c))

                                # map_w_anti[ar][ac] = "#"
                                # print_map(map_w_anti)

                                ar = ar + dr
                                ac = ac + dc

                1 == 1

    print(f"p2: {p2}")
    print(f"")

def main():
    # part1()
    part2()

if __name__=='__main__':
    main()