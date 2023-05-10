def saveThePrisoner(n, m, s):
    warn = (s + m - 1) % n
    if warn == 0:
        return n
    return warn
