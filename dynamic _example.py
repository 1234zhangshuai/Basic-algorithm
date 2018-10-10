
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

# 动态规划思想  dp方程式如下
# dp[0] = 0
# dp[i] = min{dp[i - coins[j]] + 1}, 且 其中 i >= coins[j], 0 <= j < coins.length
# 回溯法，输出可找的硬币方案
# path[i] 表示经过本次兑换后所剩下的面值，即 i - path[i] 可得到本次兑换的硬币值。


# def changeCoins(coins, n):
#     if n < 0:
#         return None
#     dp, path = [0] * (n + 1), [0] * (n + 1)  # 初始化
#     for i in range(1, n + 1):
#         minNum = i  # 初始化当前硬币最优值
#         for c in coins:  # 扫描一遍硬币列表，选择一个最优值
#             if i >= c and minNum > dp[i - c] + 1:
#                 minNum, path[i] = dp[i - c] + 1, i - c
#         dp[i] = minNum  # 更新当前硬币最优值
#
#     print('最少硬币数:', dp[-1])
#     print('可找的硬币', end=': ')
#     while path[n] != 0:
#         print(n - path[n], end=' ')
#         n = path[n]
#     print(n, end=' ')
#
#
# if __name__ == '__main__':
#     coins, n = [1, 4, 5], 22  # 输入可换的硬币种类，总金额n
#     changeCoins(coins, n)
