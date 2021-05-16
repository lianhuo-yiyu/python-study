# Python 学习 1
# 2020/11/8 11:25
#生成随机数range()
#a = range(10)
#print(list(a))

b = range(2, 10)
print(list(b))

c = range(2, 10, 2)
print(list(c))

#判断一个数在不在生成的列表中
#print(9 in a)
print(9 in c)

#while的循环 1、初始化变量   2、条件判断    3、条件执行体（循环的部分）    4、改变判断的变量
a = 0
sum = 0
while a < 10 :
    sum+=a
    a+=1
    print('累加', sum)

