# Python 学习 1
# 2020/11/29 15:41
#封装  将数据的属性和方法（数据和行为）包装到一个类对象中，在类对象外部直接调用的方法。   如果希望类中的属性不在类外部被调用，就加两个__,其实没用
#继承
#多态
class Student:
    def __init__(self, name, age):
        self.name =name
        self.age = age
    def hobby(self):
        print(self.name , 'like in' , self.age)
stu = Student('唐三', 24)
stu.hobby()

#继承 提高代码的复用性  语法 class 子类类名（父类1，父类2）  继承相关的还有重写
#弄个Student的子类  定义子类必须在构造函数中调用父辈的构造函数
class Study(Student):
    def __init__(self,like, dislike,name, age):
        super().__init__(name,age)
        self.like = like
        self.dislike = dislike
stu1 = Study('dsa',45,'PLAY', 'SLEEP')
stu1.hobby()
