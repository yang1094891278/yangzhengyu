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
练习：10个学生的成绩，需要录入系统中。
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
