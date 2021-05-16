# Python 学习 1
# 2020/11/30 17:26
#Object是所有类的父类，默认继承
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
stu = student('python',110)
print(dir(stu))
print(type(stu))
print(stu)
#对于从父类中继承的属性方法，如果使用不满意，可以对其进行重写
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return '我叫{0}，目前{1}'.format(self.name, self.age)
stu = Student('python',110)
print(dir(stu))
print(stu)