# Python 学习 1
# 2020/11/5 15:15
# 比较运算的输出结果是bool类型
a = 9
b = 5
print('a>b', a > b)
print('a<b', a < b)
print('a=b', a == b) #又一次赋值与等于写错，切记

#补充    一个变量是由三部分组成的，分别是value，ID，type ，==比较的两个的值，is比较的是标识，也就是ID
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst1 == lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))
