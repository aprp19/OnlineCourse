def hurdleRace(k, height):
    count = 0
    for i in height:
        if i > k:
            count += i - k
            k = i
    return count


print(hurdleRace(1, [1, 2, 3, 3, 4,5]))
