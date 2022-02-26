#方法的定义=函数
#自定义函数
"""
自动判断账号长度5-8位，密码6-12位，并且账号必须小写开头
def checkname (username):
  '''自动判断账号长度5-8位，密码6-12位，并且账号必须小写开头'''
    if len(username) >= 5 and len(username) <= 8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            print("OK")
        else:
            print("账号必须是小写字母开头")
    else:
        print("账号长度不符合规范，请输入5-8位的账号")
#def 方法的声明
#checkname 方法的名字 唯一
#username 方法的参数
#'''方法的说明'''
#里面的东西方法的逻辑代码
checkname("ffdadad")
"""
"""
def jiafa(a,b):
    '''
    两个数字相加
    '''
    if type(a) is int and type(b) is int:
        print(a+b)
    else:
        print("请输入数据类型不正确")
jiafa(4,5)
print(jiafa(4,5))
"""
#方法的返回值 return返回后可以对这个值做其他操作 print不能(print返回的none)
# def jiafa(a,b):
#     '''
#     两个数字相加
#     '''
#     if type(a) is int and type(b) is int:
#         return a+b
#     else:
#         print("请输入数据类型不正确")
# print(jiafa(4,5))




# #异常捕获  代码报错就是异常
# try:
#     print("a"+1)
# except:
#     print("上面代码写错了")

# # 异常类   包->类->方法->变量 既包 含又并列 Exception处理代码报错的
# try:
#     print(ddd+1)
# except Exception as e:
#     print("上面代码写错了",e)

#代码的单位  包 模块 类 方法 变量 

