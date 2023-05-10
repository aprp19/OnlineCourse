def circularArrayRotation(a, k, queries):
    b = []
    for i in queries:
        b.append(a[(i - k) % len(a)])
    return b


print(circularArrayRotation([3, 4, 5], 2, [1, 2]))
