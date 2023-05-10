def climb_leaderboard(ranked, player):
    res = []
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)
    rank = 0

    for i in range(len(player)):
        while rank < len(ranked) and player[i] < ranked[rank]:
            rank += 1
        res.append(rank + 1)

    return res[::1]


print(climb_leaderboard([100, 90, 80, 90], [70, 80, 105]))
