# def plusMinus(arr):
#     # Write your code here
#     pos = 0
#     neg = 0
#     neu = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             pos += 1
#         elif arr[i] == 0:
#             neu += 1
#         else:
#             neg += 1
#     print(pos / len(arr))
#     print(neg / len(arr))
#     print(neu / len(arr))

def plusMinus(arr):
    data = {'pos': 0,
            'neg': 0,
            'neu': 0}

    for i in arr:
        if i > 0:
            data['pos'] += 1
        elif i == 0:
            data['neg'] += 1
        else:
            data['neu'] += 1
    print(data['pos'] / len(arr))
    print(data['neg'] / len(arr))
    print(data['neu'] / len(arr))
