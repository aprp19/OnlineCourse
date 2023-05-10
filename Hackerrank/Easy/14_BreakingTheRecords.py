def breakingRecords(scores):
    maxi = scores[0]
    mini = scores[0]
    maxCount = 0
    minCount = 0
    for i in range(len(scores)):
        if scores[i] > maxi:
            maxi = scores[i]
            maxCount += 1
        if scores[i] < mini:
            mini = scores[i]
            minCount += 1
    return [maxCount, minCount]
