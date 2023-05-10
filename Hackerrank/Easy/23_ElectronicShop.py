# def getMoneySpent(keyboards, drives, b):
#     if min(keyboards) + min(drives) > b:
#         return -1
#     possibleBuys = [i + j for i in keyboards for j in drives if i + j <= b]
#
#     return max(possibleBuys)
#
#

def getMoneySpent(keyboards, drives, b):
    possibleBuys = []

    if min(keyboards) + min(drives) > b:
        return -1
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                possibleBuys.append(i + j)

    return max(possibleBuys)


print(getMoneySpent([5, 8, 3], [8, 1, 9, 5], 15))
