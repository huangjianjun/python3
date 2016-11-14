# coding = utf-8
# created by huang jian jun

# 函数的__name__属性，可以获取函数的函数名
def now():
    print("2015-10-17")
now()
print(now.__name__)

'''
安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。
不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，
因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3。
第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，
可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，
因此，安装Pillow的命令就是： pip3 install Pillow
耐心等待下载并安装后，就可以使用Pillow了。
有了Pillow，处理图片易如反掌。随便找个图片生成缩略图：
'''
from PIL import Image
im = Image.open(r"C:\Users\Administrator\Desktop\test.png")
print(im.format, im.size, im.mode)
im.thumbnail((320, 240))
im.save(r"C:\Users\Administrator\Desktop\thumb.jpeg", 'JPEG')
im = Image.open(r"C:\Users\Administrator\Desktop\thumb.jpeg")
print(im.format, im.size, im.mode)


# 在Python中，定义类是通过class关键字：
'''
class Student(object):
    pass
class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
'''
class Student(object):
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def print_name(self):
        print("name: %s" % self.name)

    def print_scores(self):
        print("scores: %s" % self.scores)

    def print_every_info(self):
        print("name: %s   scores: %s" % (self.name, self.scores))

'''
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
但self不需要传，Python解释器自己会把实例变量传进去
'''
huangjianjun = Student("huangjianjun", 97)
liujing = Student("liujing", 96)
huangjianjun.print_every_info()  # name: huangjianjun   scores: 97
huangjianjun.print_name()  # name: huangjianjun
huangjianjun.print_scores()  # scores: 97


# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):  # 继承
    def run(self):  # 多态
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))  # 判断数据类型
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

c.run();
d.run()
run_twice(c)