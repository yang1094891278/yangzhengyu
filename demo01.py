#python的常见类型
# print("hello world!")   #字符串 str
# print(233)   #整数 int
# print(1.2)   #小数 float
# print(True)   #布尔值 True False 
# print(())     #元组 tuple
# print([])    #数组 list
# print({})    #字典 dict
#空 None

# print("哈哈哈",2333,1.2)  #用逗号隔开
# print("哈哈哈"+"嘻嘻嘻")
# print("哈"*10)
# print(1+55)
# print(3>2)
# print(1+1==3)


# #变量  赋值
# a = input("请输入:")
# print("输出:",a)


# #type 读取数据的类型
# print(type(1.2),type("你好"),type(2),type(True),type(()),type([]),type({}))

# #数据类型转换
#规律  任何数据都可以转换成字符串  除了空None
#小数和整数可以互相转换
#字符串转换其他类型数据 必须满足长得像的规律
# a=int("2333")
# print(type(a))

# a = float (input("请输入："))
# b = float (input("请输入："))
# print("输出：",a+b)
# #计算字符串的长度
# a = "diuaidha udahd"
# print(len(a))

# #练习 
# a = input("请输入:")
# b = input("请输入:")
# print("a+b的长度:",len(a)+len(b))

# #元组
# a = (1,2,3,"你好",True,2,3)
# print(a)
# #只想输出一个值
# print(a[1])
# #方法：count（）统计某个值个数和index（）查找某个值下标 
# print(a.count(2))
# #下标是就近原则 显示   index()里面只能有一个值
# print(a.index(3)) 
#切片  同时取多个值  左闭右开  
# print(a[0:5])

# #二维元组
# a = (1,2,3,"你好",True,2,3)
# b = (a,57,"你好")
# #b里面一共有3个值
# print(b[1])
# #取出a里面的2
# print(b[0][1])