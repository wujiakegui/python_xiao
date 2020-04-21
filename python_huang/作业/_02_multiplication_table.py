"""
输出乘法口诀表(九九表)
Author: 笑笑
Data：20200211
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()