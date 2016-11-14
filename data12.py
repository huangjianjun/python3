#!/usr/bin/env python3.5
# coding = utf-8
# created by huang jian jun

import re

test_str = input("请输入表达式(^\d{3}\-\d{3,8}$)：")
if re.match('^\d{3}\-\d{3,8}$', test_str): # 匹配开始3个数字，中间-，以3到8之间的数字结尾(不包括3和8)
    print("matched!")
else:
    print("match failed!")

# 使用正则表达式切分字符串
ls1 = []
str1 = "a  b c, d-e;;;;f"
ls1 = re.split(r'[\s\,\-\;]+', str1) # 以一个或者多于一个的空格、逗号、短杠或者是分号来分隔
print(ls1) # result: ['a', 'b', 'c', 'd', 'e', 'f']


# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。
# 比如：^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
print("m.group(0) = %s" % m.group(0))
print("m.group(1) = %s" % m.group(1))
print("m.group(2) = %s" % m.group(2))  # m.group(0) = 010-12345  m.group(1) = 010  m.group(2) = 12345


# 时间显示
from datetime import datetime
nn = datetime.now()
print(nn.strftime('%Y-%m-%d %H:%M:%S'))
#  2016-11-01 21:59:44
