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
# #切片  同时取多个值  左闭右开  
# print(a[0:5])

# #二维元组
# a = (1,2,3,"你好",True,2,3)
# b = (a,57,"你好")
# #b里面一共有3个值
# print(b[1])
# #取出a里面的2
# print(b[0][1])


# #元组和数组的区别 一旦写好后元组不能修好 数组可以修改
# #数组
# a =  [1,2,3,"你好",True,2,3]
# print(a[4])
# #方法:
# #1、追加数据  在尾巴上追加
# a.append("append")
# print(a)
# #2、count（）统计某个值个数和index（）查找某个值下标
# #下标是就近原则 显示   index()里面只能有一个值
# print(a.count(2))
# print(a.index(3))
# #3、往数组中准确的插入数据 insert（位置，数据）
# a.insert(0,"insert")
# print(a)
# #4、类似于剪切的作用 吧值从数组中拿出来去别的地方用 pop()
# b =  [1,2,3,"你好",True,2,3]
# print(b)
# c = b.pop(3)
# print(b)
# print(c)
# #5、清空数据 clear()
# b.clear()
# print(b)
# #6、数组往数组里面装  extend（）
# xx = ["哈哈",123]
# b.extend(xx)
# print(b)
# #可以直接print（xx+b）
# #移除 remove（值）
# b.remove(123)
# print(b)

# #字典
# '''
# 特点：
# 1、字典中的值没有顺序 
# 2、字典的结构必须是键值对（key：value） 的结构
# '''
# a = {"name":"张三","age":25}
# #取值a[key]
# print(a["name"])
# #新增 
# a["high"] = "175cm"
# #修改
# a["name"]= "李四"
# print(a)
# #方法：
# #取值 get（） 取值不存在时 返回空值None
# b = a.get("name")
# print(b)
# #剪切 pop（）
# c = a.pop("high")
# print(a)
# #更新 update()
# a.update(name = 123)
# print(a)