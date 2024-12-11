def part1():
    map = [
        [int(n) for n in list(line)]
        for line in open("2024/10/input.txt").read().split("\n")
    ]

    nrow = len(map)
    ncol = len(map[0])

    dirs = [
        (  0,  1), # right
        ( -1,  0), # up
        (  0, -1), # left
        (  1,  0)  # down
    ]

    trailheads = []
    for ir, r in enumerate(map):
        for ic, c in enumerate(r):
            if c == 0:
                trailheads.append((ir,ic,c))

    trails = [[trailhead] for trailhead in trailheads] # [[[r1, c1, 0], [r2, c2, 1], ..],[[r1, c1, 0],...]]]

    completed_trails = []
    completed_pairs = set()
    while trails:
        trail = trails.pop(0)
        e = trail[-1][2] # elevation
        if e != 9:
            for d in dirs:
                ir = trail[-1][0] + d[0]
                ic = trail[-1][1] + d[1]
                if 0<= ir < nrow and 0<= ic < ncol:
                    e_next = map[ir][ic]
                    if e_next == e+1:
                        new_trail = trail + [(ir, ic, e_next)]
                        trails.append(new_trail)
                        flag = True
                        1 == 1
            if not flag: # Then there were no viable steps
                trails.pop(0)
        elif e == 9:
            completed_trails.append(trail)
            completed_pairs.add((trail[0], trail[-1]))

    p1 = len(completed_pairs)
    p2 = len(completed_trails)
    print(f"{p1=}")
    print(f"{p2=}")

    1 == 1








    1==1

def main():
    part1()

if __name__=='__main__':
    main()