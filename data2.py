import math

# 循环模式 for

ls = ["huang", "jian", "jun", "love", "python"]
for name in ls:
    print(name)

ls2 = list(range(101))
# print(ls2)
s1 = 0
for x in ls2:
    s1 += x
print("sum1 = %d " % s1)

# 循环 while <条件>

n = 100
s2 = 0
while n >= 0:
    s2 += n
    n -= 1
print("sum2 = %d " % s2)

m = 0
s3 = 0
while m < 100:
    m += 1
    if m % 2 == 0:
        continue
    s3 += m
#    print(m)
print("sum3 = %d" % s3)


m = 0
s4 = 0
while m <= 100:
    m += 1
    if m % 2 == 1:
        continue
    s4 += m
#    print(m)
print("sum4 = %d" % s4)

# 字典dict
d1 = {"huang": 2016, "jian": 10, "jun": 11}
for x in d1:
    print(x, ':', d1[x])

# 集合set
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 4, 5, 6, 8, 8]
l2 = [1, 2, 3, 9, 10]
s1 = set(l1)
s2 = set(l2)
print("max of s1 = %d " % max(s1))
print("max of s2 = %d " % max(s2))
print("s1 = %s" % s1)
print("s2 = %s" % s2)
print("s1 & s2 = %s" % (s1 & s2))
print("s1 | s2 = %s" % (s1 | s2))

number1 = 255
number2 = 512
print("hex of %d is : %s " % (number1, str(hex(number1))))
print("hex of %d is : %s " % (number2, str(hex(number2))))

# 函数的定义与使用


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operator type")
    if x >= 0:
        return x
    else:
        return -x

while True:
    c = input("c = ")
    if c == 'q':
        break
    num = int(c)
    print("abs of (%s) is: %s " % (num, my_abs(num)))

# python函数可以同时返回多个值


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x_value, y_value = move(100, 100, 60, math.pi / 6)
print("x_value = %s , y_value = %s " % (x_value, y_value))







