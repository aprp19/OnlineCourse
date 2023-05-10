def min_max_differences(list):
    pointer_max = list[0]
    pointer_min = list[0]
    for temporary_pointer in list:
        if temporary_pointer > pointer_max:
            pointer_max = temporary_pointer
        if temporary_pointer < pointer_min:
            pointer_min = temporary_pointer
    return print("Max = ", pointer_max, ", Min = ", pointer_min, ", Differences between Max and Min = ", pointer_max - pointer_min)


min_max_differences([77, 65, 23, 6, 78, 21, 45, 67, 99, 44, 31, 145])
