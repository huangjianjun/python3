# 函数的定义

def my_power(x, n):
    result = 1
    while n > 0:
        result = result * x
        n = n - 1
    return result

while True:
    x = int(input("x = "))
    if x == -1:
        break
    n = int(input("n = "))
    print("power(%s, %s) = %s" % (x, n, my_power(x, n)))


# 设置函数的默认参数
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错


def my_power_2(x, n=2):  # 函数默认在不传n的时候n = 2
    result = 1
    while n > 0:
        result = result * x
        n = n - 1
    return result

while True:
    x = int(input("x = "))
    if x == -1:
        break
    print("power(%s) = %s" % (x, my_power_2(x)))


# 学生登记信息时候好多信息都是重复的，这时设置默认参数就很方便，给函数调用带来了方便


def student_reg(name, sex, age, city = "西安市雁塔区", school = "西安邮电大学"):
    print("------------ student information -----------------")
    print("name = %s" % name)
    print("sex = %s" % sex)
    print("age = %s" % age)
    print("school = %s" % school)
    print("city = %s" % city)
    print("--------------------------------------------------")
m = 2
while m >= 1:
    name = input("name = ")
    sex = input("sex = ")
    age = int(input("age = "))
    if name == "赵锦秀":
        student_reg(name, sex, age, city="西安市长安区", school="陕西师范大学")  # 传参时修改指定默认参数的值
    else:
        student_reg(name, sex, age)
    m = m - 1



#     python 函数的可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 通常定义的函数结构如下，没有可变参数，必须事先构造一个链表或者元组


def all_power_2_1(ls):
    sum_return = 0
    for x in ls:
        sum_return = sum_return + x * x
    return sum_return

ls = [1, 2, 3,4, 5, 6, 7, 8, 9]
print("result = %s" % all_power_2_1(ls))


# 下面编写可变参数的函数构造
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：


def all_power_2_1(*numbers):
    sum_return = 0
    for x in numbers:
        sum_return = sum_return + x * x
    return sum_return
print("result1 = %s" % all_power_2_1(1, 2, 3, 4, 5, 6))
print("result2 = %s" % all_power_2_1(1, 3, 5))
print("result3 = %s" % all_power_2_1(2, 4, 6))
print("result4 = %s" % all_power_2_1())


# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去,
# *nums表示把nums这个list的所有元素作为可变参数传进去,这种写法相当有用，而且很常见。
ls2 = [1, 2, 3, 4]
print("result5 = %s" % all_power_2_1(*ls2))



# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 函数person除了必选参数name和age外，还接受关键字参数kw。也可以传入任意个数的关键字参数
# 请看示例：

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('tom', 25)  # name: tom age: 25 other: {}
person('Adam', 45, gender='M', job='Engineer', city="西安市雁塔区")
# name: Adam age: 45 other: {'job': 'Engineer', 'gender': 'M'}

# 关键字参数有什么用？它可以扩展函数的功能。
# 比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
# name: Jack age: 24 other: {'job': 'Engineer', 'city': 'Beijing'}
person("tim", 35, **extra)
# name: tim age: 35 other: {'city': 'Beijing', 'job': 'Engineer'}


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
def person_check(name, age, **kw):
    if 'city' in kw:
        print("city in the kw!")
    else:
        print("city not in the kw!")
    if 'job' in kw:
        print("jod in the kw!")
    else:
        print("jod not in the kw!")
    print('name:', name, 'age:', age, 'other:', kw)
person_check("huang", 25, city="西安市")
person_check("huang", 25, job="student")



# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 这种方式定义的函数如下：


def person_select(name, age, *, city, job):  # 只能接受关键字为city和job的参数， 否则会报错。
    print(name, age, city, job)
person_select("liu", 25, city="西安市", job="student")
person_select("huang", 25, city="西安市", job="student")


# 编写一个计算数组元素n次方的和的函数
'''
def sum_array_power_n(*array):
    print("array = ", end="")  # 添加 ,end="" 可以让输出不换行，横向输出
    for x in array:
        print(x, end=" ")
    print()  # 起单独换行的作用
    n = int(input("exp n = "))
    result = 0
    for x in array:
        m = n
        temp = 1
        while m >= 1:
            temp *= x
            m -= 1
        result += temp
    print("array of power(%d) is : %s" % (n, result))
sum_array_power_n(1, 2, 3, 4, 5)
sum_array_power_n(1, 4, 7)
'''
l1 = list(range(10))
print(l1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 对链表的迭代
l2 = ['huang', 3, 6, 8, 'A', 'B']
print("result: ", end="")
for x in l2:
    print(x, end="  ")
print()

# 对字典的迭代
# 迭代字典的key
d1 = {"huang": 520, "jian": 521, "jun": 522}
print("key result: ", end="")
for key in d1.keys():
    print(key, end=" ")
print()
# 迭代字典的value
print("value result: ", end="")
for value in d1.values():
    print(value, end=" ")
print()

# 同时迭代字典的key  value
print("key 和 value result: ")
for key, value in d1.items():
    print("key = %s  value = %s " % (key, value))
