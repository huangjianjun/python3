# 练习

while True:
    print("请输入a ：")
    a = int(input())
    if a == 0:
        break
    if a >= 100:
        print(a)
    else:
        print(-a)


A = int(input('请输入第一个数字：'))
B = int(input('请输入第二个数字：'))
if A > B:
    print('比较结果:', A, '>', B)
elif A == B:
    print('比较结果:', A, '=', B)
else:
    print('比较结果:', A, '<', B)


print(r"huangjianjun, "
      r"liujing"
      r"liujingbing")




#字符串的格式化输出
name = input("name:")
money = int(input("money:"))
print("%s ,你好！您本月的话费剩余: %d元。" % (name, money))


s1 = 72
s2 = 85
rate = 85/72 - 1
print("小明的成绩上升百分点：%.2f %% " % (rate*100))


ls = ['python', 'java', ['asp', 'php'], 'scheme']
print("len = %d " % len(ls))
print(ls[-1])
print(ls[0:2:1])
ls2 = []   # 空链表长度为 0
print("len_ls2 = %d " % len(ls2))

name = input("请输入您的姓名：")
weight = float(input("请输入您的体重(weight单位(KG)):"))  # 单位：kg
height = float(input("请输入您的身高(height单位(m)):"))  # 单位：m
BMI = weight / height / height
print("BMI = %.2f" % BMI)
s1 = "过轻"
s2 = "正常"
s3 = "过重"
s4 = "肥胖"
s5 = "严重肥胖"
if BMI <= 18.5:
    print("%s ，您的体型：%s" % (name, s1))
elif BMI > 18.5 and BMI <= 25:
    print("%s ，您的体型：%s" % (name, s2))
elif BMI > 25 and BMI <= 28:
    print("%s ，您的体型：%s" % (name, s3))
elif BMI > 28 and BMI <= 32:
    print("%s ，您的体型：%s" % (name, s4))
else:
    print("%s ，您的体型：%s" % (name, s5))


