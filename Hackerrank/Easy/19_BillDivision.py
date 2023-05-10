def bonAppetit(bill, k, b):
    total_harga = 0
    for i in bill:
        total_harga += i
    anna = (total_harga - bill[k]) // 2
    if anna == b:
        print("Bon Appetit")
    else:
        print(abs(anna - b))
