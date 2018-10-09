
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    coins.sort()  # 给硬币从小到大排序
    dp = {0: 0}  # 生成字典dp，并且当总金额为0时，最少硬币个数为0
    for i in range(1, amount + 1):
        dp[i] = amount + 1  # 因为硬币个数不可能大于amount，所以赋值amount + 1便于比较
        for j in coins:
            if j <= i:
                dp[i] = min(dp[i], dp[i - j] + 1)
                # for i in range(1,amount + 1):
                # print('dp[%d]:'%(i), dp[i])
    if dp[amount] == amount + 1:  # 当最小硬币个数为初始值时，代表不存在硬币组合能构成此金额
        return -1
    else:
        return dp[amount]


coins = [1, 5]
amount = 11
x = coinChange(coins, amount)
print(x)

# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         dp = [-1] * (amount + 1)
#         dp[0] = 0
#         for i in range(1, amount + 1):
#             for j in range(0, len(coins)):
#                 if i >= coins[j] and dp[i - coins[j]] != -1:
#                     if dp[i] == -1 or dp[i] > dp[i - coins[j]] + 1:
#                         dp[i] = dp[i - coins[j]] + 1
#
#         return dp[amount]
