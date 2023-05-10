def largestnumber(list):
    pointer = list[0]
    for temporary_pointer in list:
        if temporary_pointer > pointer:
            pointer = temporary_pointer
    return pointer


print(largestnumber([5, 4, 1, 2, 3, 5, 8, 7]))
