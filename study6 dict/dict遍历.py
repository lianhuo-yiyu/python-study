# Python 学习 1
# 2020/11/25 15:15
a = dict(name = 'PYTHON', age = 98, like = '乒乓球')
print(a)
#字典的遍历 遍历出的是键值
for item in a:
    print(item, '8')
#遍历出键值
for item in a:
    print(a.get(item))
#列表生成式  内置函数zip   整个格式   变量 = ｛key.upper() : value for key, value in zip(key,value)｝
names = ['hhh', 'lll', 'ppp'] #列表做键做值
age = [98, 9, 8]
shencheng = {names.upper(): age for names,age in zip(names,age)}
print(shencheng)
