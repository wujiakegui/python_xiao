"""
有一个字符串
text = "aAsmr3idd4bgs7Dlsf9eAF"
请将text字符串中的数字取出，并输出成一个新的字符串。
Author: 笑笑
Date: 20200211
"""
import re
text = "aAsmr3idd4bgs7Dlsf9eAF"
print(' '.join(re.findall(r'\d+',text)))
