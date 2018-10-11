# 动态规划思想  dp方程式如下
# dp[0] = 0
# dp[i] = min{dp[i - coins[j]] + 1}, 且 其中 i >= coins[j], 0 <= j < coins.length
# 回溯法，输出可找的硬币方案
# path[i] 表示经过本次兑换后所剩下的面值，即 i - path[i] 可得到本次兑换的硬币值。


def changeCoins(coins, n):
    if n < 0:
        return None
    dp, path = [0] * (n + 1), [0] * (n + 1)  # 初始化
    for i in range(1, n + 1):
        minNum = i  # 初始化当前硬币最优值
        for c in coins:  # 扫描一遍硬币列表，选择一个最优值
            if i >= c and minNum > dp[i - c] + 1:
                minNum, path[i] = dp[i - c] + 1, i - c
        dp[i] = minNum  # 更新当前硬币最优值

    print('最少硬币数:', dp[-1])
    print('可找的硬币', end=': ')
    while path[n] != 0:
        print(n - path[n], end=' ')
        n = path[n]
    print(n, end=' ')


if __name__ == '__main__':
    coins, n = [1, 4, 5], 22  # 输入可换的硬币种类，总金额n
    changeCoins(coins, n)
