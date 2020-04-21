"""
实现判断一个数是不是回文数的函数。
123321
Author: 笑笑
Date: 20200225
"""

def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num):
        print('%d是回文素数' % num)
    else:
        print('%d不是回文素数' % num)