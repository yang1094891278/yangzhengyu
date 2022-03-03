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

# # 异常类   包->类->方法->变量 既包含又并列 Exception处理代码报错的
# try:
#     print(ddd+1)
# except Exception as e:
#     print("上面代码写错了",e)

#代码的单位  包 模块 类 方法 变量 
#包分为 自带的包 和 第三方的包  都要在最上面导入 import 包名
#很多个模块可以组成包
#自带的
"""
用包要先导入 在最上方用import 
import time#控制时间的包
import random#随机数
for i in range(10):
    time.sleep(1)#控制速度
    print(i)
a = random.randint(100,1000)#生成随机数
print(a)

红绿灯程序
import time
#from time import sleep

light = {"红灯":30,"绿灯":30,"黄灯":3}
for i in light:
    for j in range(light[i]):
        time.sleep(1)
        #sleep(1)#速度
        print("{}已运行{}秒".format(i,light[i]-j))
"""
# #获取当前的时间
# import time
# xx = time.strftime("%Y-%m-%d %H:%M:%S")
# print(xx)


#第三方  在商城里下载  在终端cmd中输入 pip 第三方的管理工具
#pip install 包名 安装   pip uninstall 包名 卸载   pip list或者pip3 list 查看安装了那些包
#常用的第三方包
#xlrd 读取excel表 pymysql 操作数据库的 selenium web自动化的 appium app自动化的 requests接口自动化
"""
#xlrd包的练习
import xlrd

excle = xlrd.open_workbook("testdata.xlsx")#打开excle表，获取整个表的信息
table = excle.sheet_by_name("Sheet1")#选择对应的sheet表
Value = table.cell(1,1)#选择对应的值  第一个值是行 第二个值是列
print(Value)
row0 = table.row_values(0)#以行为单位
print(row0)
col0 = table.col_values(0)#以列为单位
print(col0)

x = table.nrows #获取一共有多少行
y = table.ncols #获取一共有多少列
print(x,y)
#整个表输出
print("-----------------------------------------------------")
for i in range(x):
    print("-----------------------------------------------------")
    rowlist = table.row_values(i)
    for j in rowlist:
        print(j,end = "\t|")
    print("")
  """

"""
#selenium 包 控制浏览器 实现网站自动化测试的功
#下载浏览器的驱动 下载最接近的版本
#吧驱动放到项目文件夹
from selenium import webdriver
import time 
driver = webdriver.Chrome(executable_path="chromedriver.exe")#对浏览器初始化
time.sleep(3)
driver.get("https://baidu.com")#打开百度
driver.find_element_by_id("kw").send_keys("小课堂") #根据id 查找输入框 输入数据
time.sleep(3)
driver.find_element_by_id("su").click()  #点击搜索按钮
time.sleep(3)
driver.quit()#退出浏览器
"""


















