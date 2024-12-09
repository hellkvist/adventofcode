def part1():
    mess = [
        list(line)
        for line in open("2024/4/input.txt", "r").read().split("\n")
        ]
    nrow = len(mess)
    ncol = len(mess[0])

    p1 = 0
    drdc = [
        ( 0, 1),
        (-1, 1),
        (-1, 0),
        (-1,-1),
        ( 0,-1),
        ( 1,-1),
        ( 1, 0),
        ( 1, 1)
    ]
    for ir, r in enumerate(mess):
        for ic, c in enumerate(r):
            if c == "X":
                for (dr, dc) in drdc:
                    word = ""
                    try: # in this direction
                        for i in range(4):
                            irr = ir+dr*i
                            icc = ic+dc*i
                            if irr >= 0 and icc >= 0:
                                word+= mess[ir+dr*i][ic+dc*i]
                        if word == "XMAS":
                            p1 += 1
                    except IndexError:
                        pass

    print(f"{p1=}")
    1 == 1

def part2():
    mess = [
        list(line)
        for line in open("2024/4/input.txt", "r").read().split("\n")
        ]
    nrow = len(mess)
    ncol = len(mess[0])

    p2 = 0
    drdc = [
        (-1, 1),
        (-1,-1),
        ( 1,-1),
        ( 1, 1)
    ]
    MAS = ["M", "A", "S"]
    seen = set()
    for ir, r in enumerate(mess):
        for ic, c in enumerate(r):
            if c == "A":
                for (dr, dc) in drdc:
                    try:
                        rs = [ir - dr*1, ir, ir + dr*1]
                        cs = [ic - dc*1, ic, ic + dc*1]
                        if -1 not in rs and -1 not in cs:
                            word1 = [
                                mess[rr][cc] for rr, cc in zip(rs, cs)
                            ]
                            if word1 == MAS:
                                for (drr, dcc) in drdc:
                                    if (drr, dcc) != (dr, dc) and abs(drr)+abs(dcc) == abs(dr)+abs(dc):
                                        try:
                                            rrs = [ir - drr*1, ir, ir + drr*1]
                                            ccs = [ic - dcc*1, ic, ic + dcc*1]
                                            if -1 not in rrs and -1 not in ccs:
                                                word2 = [
                                                    mess[rr][cc] for rr, cc in zip(rrs, ccs)
                                                ]
                                                if word2 == MAS:
                                                    if (ir,ic) not in seen:
                                                        seen.add((ir, ic))
                                                        p2 += 1
                                        except:
                                            pass # this direction
                    except IndexError:
                        pass

    print(f"{p2=}")
    1 == 1

def main():
    # part1()
    part2()

if __name__=='__main__':
    main()