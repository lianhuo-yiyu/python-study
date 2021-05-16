# Python 学习 1
# 2020/11/9 16:43
#3*3矩形
'''for i in range(1,4):
    for j in range(1,4):
     print('*', end = '\t')#/t是不换行输出
    print()#打印行
'''

#三角形
for i in range(1,7):
    for j in range(i-1, i):
        print('*' * i, end = '\t')
        print()

#乘法表
for i in range(1, 10):
    for j in range(1, i+1):
       print(i,'*', j, '=', i*j, end='\t')
    print()

#金字塔
for i in range(10):
    for j in range(1):
        a = '*' * i
    print(a.center(10, ' '))

for o in range(1,10,2):
    s=f'{"*"*i}'
    print(s.center(9,' '))