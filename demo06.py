#类  用class定义  名称首字母用大写
#特点 类的继承、重写、实例化
#面向对象编程  就是对一个对象编写它的属性
"""  """

class Car:
    def __init__(self,color,lunzi,renshu,moshi):
        self.color = color
        self.lenzi = lunzi
        self.renshu = renshu
        self.moshi = moshi
    def kaiche(self,x):
        print("一辆{}的{}汽车正在行驶".format(self.moshi,self.color))
        print("这是我传入的变量： ",x)
    def xiuche(self):
        print("我们的汽车{}个轮子坏了一个!正在修理".format(self.lenzi))

car = Car("蓝色",4,6,"手动挡")#实例化
xx = car.color
car.kaiche(222)
car.xiuche()
print(xx)

#类的继承  Newcar 继承了 Car 的类   Car就是Newcar的父类
class Newcar(Car):
    #类的重写
    def xiuche(self):
        print("对修车的方法进行了重新的定义")


newcar = Newcar("黄色",3,3,"自动挡")
newcar.kaiche(1111)
newcar.xiuche()

