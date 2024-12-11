from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
def part1():
    stones = [
        int(n)
        for n in open("2024/11/input.txt").read().split(" ")
    ]

    blinks = 10

    print(" ".join([str(s) for s in stones]))
    for b in range(blinks):
        new_stones = []
        for i, s in enumerate(stones):
            s_str = str(s)
            ls = len(s_str)
            if s == 0:
                new_stones.append(1)
            elif ls % 2 == 0:
                s0 = int(s_str[0:ls//2])
                s1 = int(s_str[ls//2::])
                new_stones.append(s0)
                new_stones.append(s1)
            else:
                new_stones.append(s*2024)
        stones = [s for s in new_stones]

        print(" ".join([str(s) for s in stones]))

    p1 = len(stones)
    print(f"{p1=}")

    1 == 1

def blink_stone(s) -> dict:
    s_str = str(s)
    ls = len(s_str)
    if s == 0:
        return {1: 1}
    elif ls % 2 == 0:
        s0 = int(s_str[0:ls//2])
        s1 = int(s_str[ls//2::])
        if s0 == s1:
            return {s0: 2}
        else:
            return {s0: 1, s1: 1}
    else:
        return {s*2024: 1}

def part2():
    stones = [
        int(n)
        for n in open("2024/11/input.txt").read().split(" ")
    ]

    blinks = 75

    stones = {s: 1 for s in stones}
    mapper = {s: blink_stone(s) for s in stones}
    for b in range(blinks):
        new_stones = {}
        for s, c in stones.items():
            if s in mapper.keys():
                new_stones_s = mapper[s]
            else:
                new_stones_s = blink_stone(s)
                mapper[s] = new_stones_s
            for n, cn in new_stones_s.items():
                if n in new_stones.keys():
                    new_stones[n] += c*cn
                else:
                    new_stones[n] = c*cn
            1 == 1
        stones = new_stones

    p2 = 0
    for k, v in stones.items():
        p2 += v
    print(f"{p2=}")

def main():
    # part1()
    # print()
    part2()

if __name__=='__main__':
    main()