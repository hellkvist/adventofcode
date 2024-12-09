def old():
    eqs = {int(line.split(": ")[0]): [int(num) for num in line.split(": ")[1].split()] for line in open("2024/7/input.txt").read().split("\n") }
    valid = []
    p1 = 0
    for LHS, RHS in eqs.items():
        valid.append(LHS)
        p1 += LHS
        tree = [LHS]

        for n in list(reversed(RHS)):
            tree = [tree_i-n for tree_i in tree]
            tree += [tree_i/n for tree_i in tree if tree_i % n == 0]

        if 0 not in tree and 1 not in tree:
            LHS = valid.pop()
            p1 -= LHS

    p1 = sum(valid)
    print("p1: " + str(p1))
    1 == 1

def main():
    eqs = {int(line.split(": ")[0]): [int(num) for num in line.split(": ")[1].split()] for line in open("2024/7/input.txt").read().split("\n") }
    valid = []
    p1 = 0
    for LHS, RHS in eqs.items():
        paths = [[RHS.pop(0)]]
        for n in RHS:
            path = []
            for p in paths[-1]:
                path.append(p+n)
                path.append(p*n)
            paths.append(path)
        if LHS in paths[-1]:
            valid.append(LHS)
            p1 += LHS
    print(f"p1: {p1}")

    eqs = {int(line.split(": ")[0]): [int(num) for num in line.split(": ")[1].split()] for line in open("2024/7/input.txt").read().split("\n") }
    valid = []
    p2 = 0
    for LHS, RHS in eqs.items():
        paths = [[RHS.pop(0)]]
        for n in RHS:
            path = []
            for p in paths[-1]:
                path.append(p+n)
                path.append(p*n)
                path.append(int(str(p) + str(n)))
            paths.append(path)
        if LHS in paths[-1]:
            valid.append(LHS)
            p2 += LHS
    print(f"p2: {p2}")

if __name__=='__main__':
    main()