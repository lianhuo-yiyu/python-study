#元组 不能进行增删改，也就是加入不进去元素  元组小括号（）
#元组的创建
#元组比较蠢，tuple()时要有两个括号    typle直接=（）时可以直接不写括号,所以一定要和str的多个赋值分清楚     tuple里面只有一个的时候，一定要有一个括号个，号
a = ('name', 45, 78, 'hhh')
c = 'll', 'jj', 'aa'
print(type(c))
print(type(a))
d,c,e = 'qq', 'ww', 'ee'
print(d, c, e)
print(type(e))
lo = ('ff',)
print(type(lo))
b = tuple(('age', 'gg', 79))
print(type(b))

#元组的遍历
for item in a:
    print(item)