def color_invert(rgb):
    convert = []
    for i in rgb:
        convert.append(255 - i)
    return tuple(convert)


print(color_invert((165, 170, 221)))