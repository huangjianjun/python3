#!/usr/bin/env python3.5
# coding = utf-8
# created by huang jian jun


# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict：

from collections import defaultdict
dd = defaultdict(lambda : 'N/A')
dd["key1"] = "huangjianjun"
print(dd["key1"],"\n",dd["key2"])

# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：

from collections import OrderedDict
d = {'a': 1, 'b': 2, 'c': 3, 'x': 5, 'y': 6}
for key in d:
    print("%s : %s" %(key, d[key]))  # 这时候KEY的取值不是按照字典创建时候键值的顺序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('x', 5), ('y', 6)])
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('x', 5), ('y', 6)])
for key in od:
    print("%s : %s" %(key, d[key]))  # 这时候KEY的取值就会按照字典创建时候键值的顺序


# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in "huangjianjun":
    c[ch] = c[ch] + 1
print(c)  # Counter({'n': 3, 'u': 2, 'a': 2, 'j': 2, 'i': 1, 'g': 1, 'h': 1})

print(c.keys())  # dict_keys(['n', 'g', 'j', 'i', 'a', 'h', 'u'])

# Counter实际上也是dict的一个子类.
for x in c.keys():  # u : 2 ## n : 3 ## i : 1 ## g : 1 ## j : 2 ## a : 2 ## h : 1 ##
    print("%s : %s" %(x, c[x]), end=' % ')


# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431955007656a66f831e208e4c189b8a9e9f3f25ba53000#0
# 关于 python 中struct的应用
'''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下： 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
'''
import io, struct
# format
# <         little-endian
# >         big-endian
# c         char            (1 byte)
# I         unsigned int    (4 bytes)
# H         unsigned short  (2 bytes)


# 获取前30个字节(头字节)
def get_header_bytes(path):
    with io.open(path, 'rb') as file:
        header_bytes = file.read(30)
        print("\n\n",header_bytes)
        return header_bytes

# 检查位图
def check_bitmap(byte):
    t = struct.unpack('<ccIIIIIIHH', byte)
    if t[0:2] == (b'B', b'M'):
        print('文件属于Windows位图')
        print('文件大小: %d' % t[2])
        print('分辨率: %d*%d' % (t[6], t[7]))
        print('颜色数: %d' % t[9])
    elif t[0:2] == (b'B', b'M'):
        print('文件属于OS/2位图')
    else:
        print('文件类型未知')

path = r'C:\Users\Administrator\Desktop\test.bmp'
b = get_header_bytes(path)
if len(b) == 30:
    check_bitmap(b)
else:
    print('文件读取失败')


''' 执行结果：
文件属于Windows位图
文件大小: 111990
分辨率: 1080*823
颜色数: 1
'''
