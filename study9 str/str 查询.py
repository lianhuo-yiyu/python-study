# Python 学习 1
# 2020/11/26 14:58
#字符串的查找操作类似于列表   index()查找字符第一次出现的位置，没有报错 find一样，没有返回-1           rindex查找子串最后一次出现的位置，rfind找不到返回-1
a = 'hello,helol,hhh'
print(a.index('lo'))
print(a.find('lo'))
print(a.rindex('hh'))
print(a.rfind('hh'))