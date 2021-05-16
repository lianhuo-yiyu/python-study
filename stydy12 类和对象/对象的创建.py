# Python 学习 1
# 2020/11/29 12:06
#创建类里面的对象  也叫做类的实例化
#语法 实例名/对象名 = 类名（）   （）里面是写的def init里面的那几个参数

#类的组成 ： 类属性、实例方法、静态方法、类方法    属性=变量    方法 = 函数   对象是定义完类之后出现的，具有类的所有属性的变量
class Lei:
    # 在类当中方法外定义的变量称为类属性，对该类的所以对象共享 类似于类里面的全局变量
    location = '北凉'
    def __init__(self, name, age):#self.name是一个实体属性，进行了一个赋值的操作，把局部变量的name赋值给了实体属性self
        self.name = name
        self.age = age
#实例方法
    def like(self):
        print('实例方法里面必须是self，然后再init就是self.valve\n ',self.age)
        print(self.name + '喜欢python')
#静态方法
    @staticmethod
    def method():
        print('用staticmethod修饰，并且（）里没有值的就是静态方法')
#类方法
    @classmethod
    def hi(cls):
        print('cls在括号里，classmethod修饰的是类方法')
#def在class外叫函数，在class内就叫做方法

#语法 实例名/对象名 = 类名（）   （）里面是写的def init里面的那几个参数
stu = Lei('hhh', 24)   #创建了一个stu对象
stu1 = Lei('AI',25)
print(id(stu))
print(type(stu))
print(stu)

stu.like()     #对象名.方法名  调用对象和对应的方法，产生结果
stu.method()
stu.hi()
'''上面三行和下面的三行等价,但同样的只有有self的地方必须有对象的名称，类方法和静态方法的（）中不允许有对象名'''
Lei.like(stu)
Lei.method()   #类名.方法名
Lei.hi()

#类属性的使用
print(stu.location)
#类属性一修改就是所有的部分都会变，全局变量的改变

#类方法是使用 不传入对象，直接用类名使用 静态方法的使用也一样
#类方法的使用
Lei.hi()
#静态方法的使用
Lei.method()

#在创建的类中动态的绑定属性和方法  为创建的对象动态绑定
#动态绑定一个属性
stu1.hobby = 'python'
print(stu.name,stu.age)
print(stu1.hobby,stu1.name,stu1.age)
#动态绑定一个方法
def show():
    print('class里面叫方法，class外面叫函数')
stu1.show = show
stu1.show()

