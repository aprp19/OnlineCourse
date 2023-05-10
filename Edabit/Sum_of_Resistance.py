def series_resistance(lst):
    pointerList = 0
    for i in lst:
        pointerList = pointerList + i
    return str(pointerList) + " ohms" if pointerList > 1.0 else str(pointerList) + " ohm"

print(series_resistance([0.5,0.5]))
# https://edabit.com/challenge/gzmFeaXwFv8X6pBGq