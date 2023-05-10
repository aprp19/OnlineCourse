def diagonalDifference(arr):
    result_kiri_ke_kanan = 0
    result_kanan_ke_kiri = 0

    for i in range(0, len(arr)):
        result_kiri_ke_kanan += arr[i][i]
        result_kanan_ke_kiri += arr[i][len(arr) - 1 - i]
    return abs(result_kiri_ke_kanan - result_kanan_ke_kiri)


# def diagonalDifference(arr):
#     l, r = 0, 0
#     for i in range(len(arr)):
#         l += arr[i][i]
#         r += arr[i][-i-1]
#     return abs(l-r)

a = [[5, 4, 2],
     [6, 5, 8],
     [1, 9, 5]]
print(diagonalDifference(a))
