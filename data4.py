
# --------------------------列表生成式

# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
ls1 = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ls1)

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]
ls2 = [x*x for x in range(1, 11)]
print(ls2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
ls3 = [x*x for x in range(1, 11) if x % 2 == 0]
print(ls3)  # [4, 16, 36, 64, 100]

# 还可以使用两层循环，可以生成全排列：
ls4 = [m+n for m in "ABC" for n in "XYZ"]
print(ls4)  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


import os  # 导入os模块，模块的概念后面讲到
ls5 = [d for d in os.listdir(r'C:\Users\Administrator\Desktop\python\python35工程代码')]  # os.listdir可以列出文件和目录
print(ls5)

L1 = ['Hello', 'World', 18, 'Apple', None]
ls6 = [x.lower() for x in L1 if isinstance(x, str)]  # isinstance(x, str) 类型判断
print(ls6)


'''
如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
练习
 杨辉三角定义如下：
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
利用生成器定义函数，
'''
def triangles(n):
    l1 = [1]  # #定义一个list[1]
    while True:
#        print(l1)  #打印出该list,此时函数为普通的函数
        yield l1  #打印出该list,此时函数为生成器类型的函数，保存算法
        l1 = [1] + [l1[m] + l1[m+1] for m in range(len(l1)-1)] + [1] ##计算下一行中间的值，再将两边的1加上
        if len(l1) >= n:  # 当最后一行列表的长度超过n 的值时，程序退出
            break
huang = triangles(10)  #调用打印生成器类型的函数
for x in huang:
    print(x)
# triangles(10)  #调用普通的函数




