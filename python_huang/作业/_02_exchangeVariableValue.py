"""
交换两个变量的值
Author: 笑笑
Date: 20200227
"""

def demo1(a, b):
    temp = a
    a = b
    b = temp
    print(a, b)

def demo2(a, b):
    a, b = b, a
    print(a, b)

def demo3(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)

def demo4(a, b):
    a = a ^ b
    b = a ^ b  # b = (a^b)^b = a
    a = a ^b   # a = (a^b)^a = b
    print(a, b)

a = input("a:")
b = input("b:")
demo2(2,3)