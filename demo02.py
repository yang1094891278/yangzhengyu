##判断 if 换行后必须是4个空格
##判断条件 == !=  in  is  not in  not is
# a=1
# b=2
# if a == 1 :
#     print("是1")

# if a > b :
#     print("a大") 
# else:
#     print("b大")

# age = int( input("请输入你的年龄："))
# if age > 60:
#     print("退休")
# elif age > 30:
#     print("责任重")
# elif age > 20:
#     print("好好规划未来")
# else:
#     print("好好读书")




# #in 用法  in查是否在其中  
# a = "你好"
# if a in "你好，今天你吃了吗" :
#     print("ok")
# else:
#     print("不ok")

# a = input("请输入：")
# if a == "":
#     print("不能为空")
#     exit()
# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入数字")
#     exit()
# if a > 5:
#     print("大")
# else:
#     print("小")


# #is用法   is判断类型  就是“是”的意思
# a = "jjjjk"
# if type(a) is int:
#     print("是数字！")
# elif type(a) is str:
#     print("是字符串！")
# else:
#     print("其他")





#循环  while  for  
#while循环
# a = 1
# while a < 10:
#     print("小于10")
#     a = a + 1

'''
练习：10个学生的成绩，需要录入系统中。用while写
学生：张三、李四、王麻子、浪晋、流云、希希、小二、二狗、周毅、亚索
并且名字和成绩对应   而且大于60的和小于60的需要分开存放
highchengji = {}
lowchengji = {}
studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小二","二狗","周毅","亚索"]
a = 0
while a < len(studentlist):
    chengji =int(input("请输入"+studentlist[a]+"成绩: ")) 
    if chengji >= 60:
        highchengji[studentlist[a]] = chengji
    else:
        lowchengji[studentlist[a]] = chengji
    a = a + 1
print("大于60分的： ",highchengji)
print("小于60分的： ",lowchengji)
'''


# #for循环  原理通过遍历实现的
# a = ["张三","李四","王老五","王麻子","周毅"]
# for  i in a:
#     print(i)
# #rangr(数字)方法  
# b = list(range(0,100)) #左闭右开  自动生成一个数列
# print(b)

# for i in range(100):#循环多少遍
#     print(i)

# #range（）控制它的变化
# c = list(range(0,100,2))#左闭右开  自动生成一个数列 2是步进/步长
# print(c)

''' 
练习：10个学生的成绩，需要录入系统中。  用for写
学生：张三、李四、王麻子、浪晋、流云、希希、小二、二狗、周毅、亚索
并且名字和成绩对应   而且大于60的和小于60的需要分开存放
highchengji = {}
lowchengji = {}
studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小二","二狗","周毅","亚索"]
for i in studentlist:
    chengji =int(input("请输入"+i+"成绩: ")) 
    if chengji >= 60:
        highchengji[i] = chengji
    else:
        lowchengji[i] = chengji
print("大于60分的： ",highchengji)
print("小于60分的： ",lowchengji)
'''

'''
九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end=" ")#end不会换行
    print()#换行的作用
'''
# #end的作用 不换行 冒号里面输入啥就显示啥
# a = ["张三","李四","王麻子","浪晋","流云","希希","小二","二狗","周毅","亚索"]
# for i in a:
#     print(i,end="//")
'''
练习1：通过print打印模拟红路灯的功能 红灯30次 绿灯35次 黄灯3次
练习2：使用代码实现注册的功能。用户输入账号和密码，要求账号长度5-8位，密码6-12位，
并且账号必须小写开头，储存在字典中{username：password}
'''