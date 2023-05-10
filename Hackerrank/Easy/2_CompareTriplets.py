def comparetriplets(a, b):
    aP = 0
    bP = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            aP += 1
        elif a[i] < b[i]:
            bP += 1

    return aP, bP
