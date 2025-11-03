amount = 50
change = 0


def correct_coin(coin):
    valid = [5, 10, 25]
    if coin in valid:
        return True
    else:
        return False


while amount > 0:
    coin = int(input("coin: "))
    if correct_coin(coin) == True:
        amount -= coin
    if amount < 0:
        change = -amount
    elif amount > 0:
        print("amount due: ", amount)
print("change: ", change)
