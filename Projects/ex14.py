def remove_dups1(L1, L2):
    for e in range(len(L1) - 1, -1, -1):
        if L1[e] in L2:
            L1.remove(L1[e])
        print(L1, "\n", L2)
    #print(L1, "\n", L2)


def remove_dups2(L1, L2):
    index = 0
    while index < len(L1):
        if L1[index] in L2:
            L1.remove(L1[index])
        else:
            index += 1
        print(L1, "\n", L2)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups1(L1, L2)
