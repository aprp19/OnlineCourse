def stutter(word):
    kata_potong = word[:2] + "... "
    return kata_potong + kata_potong + word + "?"


print(stutter("Outstanding"))
