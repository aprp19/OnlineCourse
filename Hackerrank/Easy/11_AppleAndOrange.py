def countApplesAndOranges(s, t, a, b, apples, oranges):
    app = org = 0
    for d in apples:
        if a + d in range(s, t + 1):
            app += 1
    for d in oranges:
        if b + d in range(s, t + 1):
            org += 1
    print(app)
    print(org)
