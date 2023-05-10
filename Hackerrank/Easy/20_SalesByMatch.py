def sockMerchant(n, ar):
    total_sock = []
    for sock in set(ar):
        total_sock.append(ar.count(sock))
    return sum([i // 2 for i in total_sock])


print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))


# def sockMerchant(n, ar):
#     count = 0
#     arr = set(ar)
#     for v in arr:
#         count += ar.count(v)//2
#     return count