def countingValleys(steps, path):
    lembah = 0
    jalur = 0
    for i in path:
        if i == 'U': jalur += 1
        if i == 'D': jalur -= 1
        if jalur == 0 and i != 'D': lembah += 1
    return lembah


print(countingValleys(8, ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']))
