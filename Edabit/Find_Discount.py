def disc(price, discount):
    discounted_price = (discount / 100) * price
    return round(price - discounted_price, 2)


print(disc(593, 61))

# https://edabit.com/challenge/cXnkmRdxqJrwdsP4n
