#!/usr/bin/env python3.5
# coding = utf-8
# created by huang jian jun


# 文件的IO操作
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
'''
try:
    fd = open(r"huang.txt", 'r')
    ret = fd.read()
    print("ret type: %s" % type(ret))
    print(ret)
finally:
    if fd:
        fd.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

with open(r"huang.txt", 'r') as fd:
    print(fd.read())  # 调用read()会一次性读取文件的全部内容

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
# 因此，要根据需要决定怎么调用。 如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
'''
with open(r"huang.txt", 'r', encoding='gbk') as fd:
    for n in range(1, 8):
        print("row %s: %s " % (n, fd.readline().strip()))
'''
with open(r"huang.txt", 'r', encoding='utf-8') as fd:
    for n in range(1, 7):
        print("row %s: %s " % (n, fd.read(50)))

num = 0
with open(r"huang.txt", 'r', encoding='utf-8') as fd:
    for line in fd.readlines():
        num += 1
        print("row %s: %s " % (num, line.strip()))  # 把末尾的'\n'删掉


with open(r'test.txt', 'w') as fd_w:  # 文件不存在自动创建
    fd_w.write('Hello, world, I love python!')
'''
with open(r'test.txt', 'a') as fd_w:  # 文件以追加方式打开
    for num in range(0, 5):
        num += 1
        fd_w.write("\ntest %s: %s " % (num, "I love python!"))

'''
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
Python提供了pickle模块来实现序列化。
'''
