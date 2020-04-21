"""
输入两个正整数计算它们的最大公约数和最小公倍数
Author: 笑笑
Date: 20200211
"""

x = int(input('请输入x的值 = '))
y = int(input('请输入y的值 = '))
if x > y:       # 如果x大于y就交换x和y的值
    x, y = y, x     # 通过下面的操作将y的值赋给x, 将x的值赋给y
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

# def gcd(x, y):
#     """求最大公约数"""
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
# def lcm(x, y):
#     """求最小公倍数"""
#     return x * y // gcd(x, y)