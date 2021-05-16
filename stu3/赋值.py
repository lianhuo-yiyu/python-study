# Python 学习 1
# 2020/11/5 14:56
a = 20
print(a)
a = b = c =20
print(a,b+c)

a+=20
print('a+=20的为',a,'所以a+=20就是a=a+20')

#解包赋值，一对一的个数，左边几个右边几个
a,b,c = 30,40,50
print(a,b,c)

#python进行值的转化，C语言里面位 a=20,b=30,c=a,a=b,b=c   就是要有中间变量
a=20
b=30
b,a=a,b
print(a,b)



