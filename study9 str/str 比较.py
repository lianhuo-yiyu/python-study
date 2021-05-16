# Python 学习 1
# 2020/11/26 20:14
print('app'>'css')#比较的是ASCII ord可以看到
print('A'>'a')
print(ord('a'))
print(ord('A'))

#== 与 is的不同在于  is比较的是id是否相等（存储地址），==比较的是value是否相等
a = b ='pop'
c = 'pop'
print(a is b)
print(a == b)