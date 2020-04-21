"""
输入一个正整数判断它是不是素数
素数：只能被1和自身整除的大于1的整数。
Author: 笑笑
Date: 20200211
"""


from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for i in range(2,end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)


# def is_prime(num):
#     """判断一个数是不是素数"""
#     for factor in range(2, num):
#         if num % factor == 0:
#             return False
#     return True if num != 1 else False

"""
输出0--100内所有素数

for i in range(2,101):
    for temp in range(2,i):
        if i % temp == 0:
            break
        if temp==i-1:
            print(i)

"""

