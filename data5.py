# python 中的高阶函数，就是将函数作为参数传入到另外一个函数中
import math
from math import sqrt
from math import tan
from math import sin

# 实现一个函数，可以接受任意多的数字，任意多的函数参数，最后输出每一种函数下每一个数字的结果
def do_number_sth(x=[], *func):
    for f in func:
        for num in x:
            if not isinstance(num, (int, float)):
                raise TypeError('bad operand type')
            print(" %s(%s): %s" % (str(f)[18:-1], num, f(num)))
        print()
print(do_number_sth([4, 9, -25, math.pi/6], abs,sin))


# map/reduce 的简单解说
#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000
'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是： reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
# 整理成一个str2int的函数就是： from functools import reduce
from functools import reduce
import types
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int("3456396"), type(str2int("3456396")))


def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def fun_10(count):
        ret = 1
        while count >= 1:
            ret *= 10
            count -= 1
        return ret
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    ls = list(s.split('.'))
    m = reduce(fn, map(char2num, ls[0]))
    n = reduce(fn, map(char2num, ls[1]))
    print("m = %d" % m)
    print("n = %d" % n)
    k = fun_10(len(ls[1]))
    result = m + n / k
    print("result = %s %s" % (result, type(result)))
    return
str2float("123.456")

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']：
'''
def do_func(name):
    ls = name[0].upper() + name[1:len(name)].lower()
    return ls
ls2 = list(map(do_func, ['adam', 'LISA', 'barT']))
print(ls2)

              # python 的排序函数sorted()

# 对数字的排序
ls = [24,35,-29,55,3]
ls1 = sorted(ls)
print(ls1)  # [-29, 3, 24, 35, 55]
ls2 = sorted(ls, key = abs)
print(ls2)  # [3, 24, -29, 35, 55]
ls3 = sorted(ls, key = abs, reverse = True)
print(ls3)  # [55, 35, -29, 24, 3]

# 对字符串的排序,默认按照ACSII值排序
st = ['bob', 'about', 'Zoo', 'Credit']
lst1 = sorted(st)
print(lst1)  # ['Credit', 'Zoo', 'about', 'bob']
lst2 = sorted(st, key = str.lower)
print(lst2)  # ['about', 'bob', 'Credit', 'Zoo']
lst3 = sorted(st, key = str.lower, reverse = True)
print(lst3)  # ['Zoo', 'Credit', 'bob', 'about']

'''
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''

ls = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
def by_score(t):
    return t[1]
l2 = sorted(ls, key = by_name)
print(l2)  # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
l3 = sorted(ls, key = by_score)
print(l3)  # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]

