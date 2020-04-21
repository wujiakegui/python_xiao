"""
从1~n中，随机取m个数。1<=m<=n
Author: 笑笑
Date: 20200211
"""
import random

n = int(input('请输入一个正整数n = '))
m = int(input('请输入一个正整数m = '))

# 第一种
for i in range(1,m+1):
    i = random.randint(1,n+1)
    print(i,end=" ")

# 第二种
i = random.sample(range(1, n), m)
print(i)