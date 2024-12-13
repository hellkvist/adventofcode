from copy import deepcopy
def part1_old():
    garden = [list(line) for line in open("2024/12/input.txt").read().split("\n")]
    crops = set()
    for r in sum(garden, []):
        crops.add(r)
    crops = sorted(crops)

    nrow = len(garden)
    ncol = len(garden[0])
    regions = {k: [] for k in crops}
    adj = [
        (  0,  1), # r
        ( -1,  1), # ur
        ( -1,  0), # u
        ( -1, -1), # ul
        (  0, -1), # l
        (  1, -1), # dl
        (  1,  0), # d
        (  1,  1), # dr
    ]
    for ir, r in enumerate(garden):
        for ic, c in enumerate(r):
            if c == "C":
                1 == 1
            if (ir, ic) not in [(iir, iic) for region in regions[c] for (iir, iic, nn) in region]:
                regions[c].append(set())
                regions[c][-1].add((ir, ic, 4))
                region = regions[c][-1]
            else:
                for region in regions[c]:
                    if (ir, ic) in region:
                        break
            pc = 4
            for id, (dr, dc) in enumerate(adj):
                if id % 2 == 0:
                    (iir, iic) = (ir+dr, ic+dc)
                    if 0 <= iir < nrow and 0 <= iic < ncol:
                        if garden[iir][iic] == c: # If adjacent plot has same crop, add to correct region
                            for (ddr, ddc) in [adj[id-1], adj[id], adj[id+1]]:
                                (iiir, iiic) = (ir + ddr, ic + ddc)
                                if 0 <= iiir < nrow and 0 <= iiic < ncol:
                                    if garden[iiir][iiic] == c:
                                        if (iiir, iiic) not in [(p[0],p[1]) for p in region]:
                                            region.add((iiir, iiic, 4))
                            pc -= 1

            p = [p for p in region if p == (ir, ic, 4)][0]
            region.remove(p)
            region.add((ir, ic, pc))
            1 == 1

    p1 = 0
    for c, c_regions in regions.items():
        for c_region in c_regions:
            fence_l = sum([n for (ir, ic, n) in c_region])
            area = len(c_region)
            p1 += fence_l*area
    print(f"{p1=}")
    1 == 1


def part1():
    garden = [list(line) for line in open("2024/12/input.txt").read().split("\n")]
    crops = set()
    for r in sum(garden, []):
        crops.add(r)
    crops = sorted(crops)

    nrow = len(garden)
    ncol = len(garden[0])
    adjacents = {k: {} for k in crops}
    adj = [
        (  0,  1), # r
        ( -1,  1), # ur
        ( -1,  0), # u
        ( -1, -1), # ul
        (  0, -1), # l
        (  1, -1), # dl
        (  1,  0), # d
        (  1,  1), # dr
    ]

    fences = {}
    for ir, r in enumerate(garden):
        for ic, c in enumerate(r):
            adjacents[c][(ir, ic)] = set()
            nfences = 4
            for id, (dr, dc) in enumerate(adj):
                if id % 2 == 0:
                    (iar, iac) = (ir+dr, ic+dc)
                    if 0 <= iar < nrow and 0 <= iac < ncol:
                        if garden[iar][iac] == c: # If adjacent plot has same crop, add to set of adjacents to ir ic
                            adjacents[c][(ir, ic)].add((iar, iac))
                            nfences -= 1
            fences[(ir, ic)] = nfences

            # adjacents[c][-1] = sorted(adjacents[c][-1])

    regions = {c: [] for c in crops}
    for c in crops:
        seen = set()
        for p, lp in adjacents[c].items():
            if p in seen:
                continue
            linked = set([p]) # [(0,28),(0,29)]
            linked.update(lp)
            notseen = set(lp) # [(0,29)]
            seen.add(p) # [(0,28)]
            while notseen:
                pp = notseen.pop() # (0,29) []
                seen.add(pp) # [(0,28),(0,29)]

                pp_linked = adjacents[c][pp] # {(0, 30), (1, 29), (0, 28)}
                for ppp in pp_linked:
                    if ppp not in seen:
                        linked.add(ppp) # [(0,28),(0,29),(0, 30), (1, 29)]
                        notseen.add(ppp) # [(0, 30), (1, 29)]
            fence_len_region = 0
            for l in linked:
                fence_len_region += fences[l]
            area_region = len(linked)
            regions[c].append((area_region, fence_len_region, linked))

    p1 = 0
    for c in crops:
        for r in regions[c]:
            p1 += r[0]*r[1]
    print(f"{p1=}")


    p2 = 0
    dir = [
        (0,1), # r
        (1,0), # d
        (0,-1), # l
        (-1,0) # u
    ]
    for c in crops:
        for a,f,rs in regions[c]:
            # find all plots that have exposed >=1 exposed side
            notseen = set()
            for p in rs:
                if fences[p] != 0:
                    notseen.add(p)
            seen = set()
            turns = 0
            # Count every time we turn until we came back to the start
            r = [r for r in rs]
            r.sort() # Sort by (row, column)
            pstart = r[0]
            idstart = 0 # right

            p = pstart
            id = idstart


            # Calculate outer sides
            while True:
                for dir_diff in [-1, 0, 1]:
                    moved_bool = False
                    d = dir[(id+dir_diff) % 4]
                    p_next = (p[0]+d[0], p[1]+d[1])
                    if p_next in r:
                        id = (id + dir_diff) % 4
                        if dir_diff == 1:
                            p = p
                            turns += 1
                        elif dir_diff == 0:
                            p = p_next
                        elif dir_diff == -1:
                            p = p_next
                            turns += 1
                        moved_bool = True
                        break
                if not moved_bool:
                    # If no node to the left, front or right, we simply just turn right
                    id = (id + dir_diff) % 4
                    turns += 1

                if p in notseen:
                    notseen.remove(p)
                    seen.add(p)

                if p == pstart and id == idstart:
                    # Then we came back to the start of the region
                    break

            # Calculate inner sides
            while notseen:
                extra_turns = 0
                l_notseen = [n for n in notseen]
                l_notseen.sort(reverse=True)
                pstart = l_notseen[0]
                notseen.remove(pstart)
                p = pstart
                if pstart not in seen:
                    seen.add(pstart)
                # determine starting direction
                # find a side of pstart which is empty
                # and put it to the right side of the starting dir
                for id, d in enumerate(dir):
                    p_right = (pstart[0]+dir[(id+1)%4][0], pstart[1]+dir[(id+1)%4][1])
                    if p_right not in r:
                        idstart = id
                        id = idstart
                        break
                1 == 1
                while True:
                    for dir_diff in [1, 0, -1]:
                        moved_bool = False
                        d = dir[(id+dir_diff) % 4]
                        p_next = (p[0]+d[0], p[1]+d[1])
                        if p_next in r:
                            id = (id + dir_diff) % 4
                            if dir_diff == 1:
                                p = p_next
                                extra_turns += 1
                            elif dir_diff == 0:
                                p = p_next
                            elif dir_diff == -1:
                                p = p
                                extra_turns += 1
                            moved_bool = True
                            break
                    if not moved_bool:
                        # If no node to the left, front or right, we simply just turn right
                        id = (id + dir_diff) % 4
                        extra_turns += 1

                    if p in notseen:
                        notseen.remove(p)
                        seen.add(p)

                    if p == pstart and id == idstart:
                        # Then we came back to the start of the region
                        break
                turns += extra_turns
            price_region = a*turns
            p2 += price_region
    print(f"{p2=}")


def main():
    part1()

if __name__=='__main__':
    main()