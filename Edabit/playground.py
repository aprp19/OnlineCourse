# def getUniqueCharacter(s):
#     frekuensi = {}
#     for i in s:
#         if i not in frekuensi:
#             frekuensi[i] = 1
#         else:
#             frekuensi[i] += 1
#     for i in range(len(s)):
#         if frekuensi[s[i]] == 1:
#             return i + 1
#     return -1
#
#
# print(getUniqueCharacter('hackthegame'))

import re
def howMany(sentence):
    # Write your code here
    replaced_string = re.sub(r'\W+', ' ', sentence)
    perKata = replaced_string.split()
    tanpaAngka = []
    count = 0
    for i in perKata:
        if not i.isdigit():
            tanpaAngka.append(i)
    for i in tanpaAngka:
        if len(i) > 1:
            count += 1
    return count

print(howMany('he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? All test-cases should pass. Done-done?'))
print(howMany('b? Dl )B 4(V! A. MK, YtG ](f 1m )CNxuNUR {PG?'))
print(howMany('jds dsaf lkdf kdsa fkldsf, adsbf ldka ads? asd bfdal ds bf[l. akf dhj ds 878  dwa WE DE 7475 dsfh ds  RAMU 748 dj.'))
#
# import re
# def howMany(sentence):
#     replaced_string = re.sub(r'\W+', ' ', sentence)
#     return replaced_string
