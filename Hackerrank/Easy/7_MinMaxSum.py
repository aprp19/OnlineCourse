def miniMaxSum(arr):
    smallest = arr[0]
    biggest = arr[0]
    for i in arr:
        if i > biggest:
            biggest = i
        if i < smallest:
            smallest = i
    return print(sum(arr) - biggest, sum(arr) - smallest)


def miniMaxSum(arr):
    sortedArray = sorted(arr)
    minSum = sum(sortedArray[:-1])
    maxSum = sum(sortedArray[1:])
    print(minSum, maxSum)
