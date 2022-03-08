#selenium 包 控制浏览器 实现网站自动化测试的功
#下载浏览器的驱动 下载最接近的版本
#吧驱动放到项目文件夹
from selenium import webdriver
import time 
driver = webdriver.Chrome(executable_path="chromedriver.exe")#对浏览器初始化
driver.get("https://baidu.com")#打开百度
#控制浏览器的大小、位置的方法
# driver.minimize_window()#最小化
# time.sleep(3)
# driver.maximize_window()#最大化
# time.sleep(3)
# size =driver.get_window_size()#获得浏览器大小
# print(size)
# time.sleep(3)
# driver.set_window_size(800,500)#调整大小
# time.sleep(3)
# position = driver.get_window_position()#获得坐标
# print(position)
# time.sleep(3)
# driver.set_window_position(500,0)#调整坐标 改变位置
# time.sleep(3)

# js = "这是js脚本"  #运行js脚本
# driver.execute_script(js)
#控制cookies的方法
# driver.get_cookie()#得到cookie
# driver.get_cookies()#得到所有cookie
# driver.add_cookie()#添加cookie
# driver.delete_all_cookies()#删除所有cookie
# driver.delete_cookie()#删除cookie

# #获取句柄（句柄相当于窗口的身份证）
# driver.window_handles()#获取当前浏览器所有的句柄
# driver.current_window_handle()#获取当前窗口的句柄
# #window窗口的切换  frame表单  allert弹窗
#driver.switch_to.window

# driver.find_element_by_id("kw").send_keys("小课堂") #根据id 查找输入框 输入数据
#driver.find_element_by_name("wd").send_keys("小课堂")#根据name定位
#driver.find_element_by_class_name("s_ipt").send_keys("小课堂")#根据class_name定位
#driver.find_element_by_css_selector("input#kw.s_ipt").send_keys("小课堂")#根据样式选择器定位
#driver.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("小课堂")#根据xpath定位  右键复制xpath 里面有" 要用\"转义 才能识别
#driver.find_element_by_tag_name("form").find_element_by_tag_name("span").find_element_by_tag_name("input").send_keys("小课堂")#根据tag_name定位 tag是标签 标签名会重复 需要一层一层的去定位
#driver.find_element_by_id("su").click()  #点击搜索按钮
# time.sleep(3)
#根据全部文字定位
# driver.find_element_by_id("kw").clear()
# time.sleep(2)
driver.find_element_by_link_text("新闻").click()
#根据部分文字定位
#driver.find_element_by_partial_link_text("全国政协").click()
time.sleep(2)
# #常见的方法
driver.switch_to.window(driver.window_handles[-1])
title = driver.title #获取网页的title
print(title)
#获取定位对象的文本
# text = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/a[1]").text
# print(text)

driver.quit()#退出浏览器
#八大定位方式：id、name、class_name、css_selector、xpath、tag_name、link_text、partial_link_text