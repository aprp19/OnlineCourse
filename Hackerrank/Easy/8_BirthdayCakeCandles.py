def birthdayCakeCandles(candles):
    largest = max(candles)
    count = 0
    for num in candles:
        if num == largest:
            count += 1
    return count
