from copy import deepcopy
def part1():
    map = [
        int(n)
        for n in list(open("2024/9/input.txt", "r").read())
    ]

    blocks = []
    id = 0
    for i, n in enumerate(map):
        if i % 2 == 0:
            blocks += [id]*n
            id += 1
        else:
            blocks += [-1]*n

    empty_is = [i for i,b in enumerate(blocks) if b==-1]

    for i in empty_is:
        while blocks[-1] == -1:
            blocks.pop()
        print(blocks[-1])
        if -1 not in blocks:
            break
        blocks[i] = blocks.pop()

    p1 = 0
    for i,b in enumerate(blocks):
        p1 += i*b
    print(f"{p1=}")
    1 == 1

def part2_bad():
    map = [
        int(n)
        for n in list(open("2024/9/input.txt", "r").read())
    ]

    blocks = []
    empty_blocks = []
    id = 0
    for i, n in enumerate(map):
        if i % 2 == 0:
            blocks.append([id]*n)
            id += 1
        else:
            empty_blocks.append([-1]*n)
    remapped = blocks[0]
    blocks.pop(0)
    while blocks:
        print(len(blocks))
        e = empty_blocks.pop(0)
        while e:
            i = -1
            b = blocks[-1]
            diff = len(e) - len(b)
            while diff < 0:
                i -= 1
                try:
                    b = blocks[i]
                    diff = len(e) - len(b)
                except IndexError: # If i becomes out of range there is no fit
                    diff = -1
                    break
            if diff == -1:
                remapped += e + blocks.pop(0)
                e = []
            else: # Move file
                b = blocks.pop(i)
                remapped += b
                e = [-1]*diff
                # We must insert empty space where the file was
                # empty_blocks.insert([-1]*)

        # Before we move to next empty block, insert the first block
        remapped += blocks.pop(0)

    p2 = 0
    for i,b in enumerate(remapped):
        if b != -1:
            p2 += i*b
    print(f"{p2=}")

def part2():
    map = [
        int(n)
        for n in list(open("2024/9/input.txt", "r").read())
    ]

    blocks = []
    id = 0
    for i, n in enumerate(map):
        if i % 2 == 0:
            blocks.append([id]*n)
            id += 1
        else:
            if n > 0:
                blocks.append([-1]*n)

    i_b = len(blocks)
    while i_b > 0:
        i_b -= 1
        b = blocks[i_b]
        print(i_b)
        if b[0] != -1:
            for i_e, e in enumerate(blocks[0:i_b]):
                if e[0] == -1:
                    if i_e < i_b: # if empty block is to the left of not empty block
                        diff_len = len(e) - len(b)
                        if diff_len >= 0: # if fits i sits
                            blocks[i_e] = b # move
                            blocks[i_b] = [-1]*len(b)# replace previous posision with empty block
                            if diff_len > 0:
                                blocks.insert(i_e+1, [-1]*diff_len)
                                i_b += 1
                            # if blocks[-1][0] == -1: # If last block is empty, remove it
                            #     blocks.pop()

                            break # check next block to move




    p2 = 0
    remapped = sum(blocks, [])
    for i,b in enumerate(remapped):
        if b != -1:
            p2 += i*b
    print(f"{p2=}")

def main():
    # part1()
    part2()

if __name__=='__main__':
    main()