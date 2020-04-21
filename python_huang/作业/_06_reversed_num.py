"""
正整数反转
例如：12345变成54321
Author: 笑笑
Date: 20200211
"""

# 常规操作
num = int(input('请输入一个正整数num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

# 将正整数转化为列表进行操作
# num = input("请输入一个正整数：")
# s = list(num)
# s.reverse()
# print(s)