# Python 学习 1
# 2020/11/25 9:45
#字典的判断是key在不在，不能判断值在不在。 值依靠键去dict.get()
zi = dict(name = 'Python', age = 500, like = 'sleep')
print(500 in zi)
print('name' in zi)

#字典的删除  删除了key,值也就被删除
del zi['like']
print(zi)

#字典的清除,直接回到空字典
zi.clear()
print(zi)

#元素的增加
zi['name'] = 'c语言'
zi['age'] = 600
zi['like'] = 999
print(zi)
#元素的修改
zi['age'] = 599
print(zi)

#获取字典视图的方法 keys()获取所有的key    values()获取所有的值     items()获取所有的键值对
a = zi.keys()
print(a)
print(list(a))
b = zi.values()
print(b)
print(list(b))
c = zi.items()  #元组
print(c)
print(list(c))