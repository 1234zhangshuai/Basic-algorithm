

import math
m, n = map(int, input().split())
for i in range(m, n):
    x = math.floor(i / 100)  # 获得百位数
    y = math.floor((i - x * 100) / 10)  # 获得十位数
    z = i - math.floor(i / 10) * 10  # 获得个位数
    if i == x ** 3 + y ** 3 + z ** 3:
        print(i, end=', ')


# for n in range(100,1000):
#     i = n / 100
#     j = n / 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print n
