#类 多个相似事物组成的群体的统称  type()获得的    如int, list, dict
#对象是类里面的相似的不同个例 如int里面的 45，64   list里的['dsa','sada']   Python里一切皆对象

#Python里面定义一个类  class 类名(类名的首字母大写)
class Student:
    pass
print(type(Student))
print(id(Student))
print(Student)

#类的组成 ： 类属性、实例方法、静态方法、类方法
#在类当中方法外定义的变量称为类属性，对该类的所以对象共享 类似于类里面的全局变量
class Lei:
    localtion = '北凉'
    def __init__(self, name, age):#self.name是一个实体属性，进行了一个赋值的操作，把局部变量的name赋值给了实体属性self
        self.name = name
        self.age = age
#实例方法
    def like(self):
        print('实例方法里面必须是self，然后再init就是self.valve')
#静态方法
    @staticmethod
    def method():
        print('用staticmethod修饰，并且（）里没有值的就是静态方法')
#类方法
    @classmethod
    def hi(cls):
        print('cls在括号里，classmethod修饰的是类方法')
#def在class外叫函数，在class内就叫做方法

#类属性的使用
print('见下页')

