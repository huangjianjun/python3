#!/usr/bin/env python3.5
# coding = utf-8
# created by huang jian jun

# 动态的添加类的方法
from types import MethodType

class student(object):
    pass

s1 = student()
s1.name = "huangngjianjun"  # # 动态给实例绑定一个属性
print(s1.name)  # huangngjianjun

def set_age(self, age):
    self.age = age

s1.set_age = MethodType(set_age, s1)  # 给实例绑定一个方法
s1.set_age(25)  ## 调用实例方法
print(s1.age)  # 25

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_scores(self, scores):
    self.scores = scores

student.set_scores = set_scores  # 给class 类绑定方法
s1.set_scores(100)
print(s1.scores)

# python 的错误判断处理文章连接
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191375461417a222c54b7e4d65b258f491c093a515000
# python 的错误判断机制 try''''except 或者 try'''''except''''''finally 模式
def divition(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError('bad operand type')
    try:
        result = num1 / num2
        print("%s/%s= %s" %(num1, num2, result))

    except ZeroDivisionError as err:
        print('except:', err)
    finally:                        # finally 可以省去不写
        print("finally: do it !")

divition(22, 5)
divition(4, 0)
divition(5, A)  # NameError: name 'A' is not defined

# 关于python 代码调试的连接
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431915578556ad30ab3933ae4e82a03ee2e9a4f70871000






