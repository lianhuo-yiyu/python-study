# Python 学习 1
# 2020/11/28 17:12
#递归函数 一个函数调用自己
#递归用来计算阶乘
def fac(n):
    if n ==1:
        return 1
    else:
        return  n *fac(n - 1)
print(fac(6))

def text(n):
    for i in range(1,n):
      if i == 1 :
          print('1')
      elif i == 2 :
          print('1','1')
      elif i != 1 and i !=2 :
          print(555 + i)
print(text(5))

