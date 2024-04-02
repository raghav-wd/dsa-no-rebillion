class Change:
    def __init__(self, one, five, seven):
        self.one = one
        self.five = five
        self.seven = seven

n = 20

coins = [7, 5]
dp = []
for _ in range(n+1):
    dp.append([])
for i in range(1, n+1):
    amount = i
    for coin in coins:
        if amount % coin == 0:
            dp[i].append(coin)
            amount = amount%coin
            print(amount)


print(dp)