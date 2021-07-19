returnCoin = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
    if coin <= returnCoin:
        count += returnCoin // coin
        returnCoin = returnCoin % coin

print(count)
