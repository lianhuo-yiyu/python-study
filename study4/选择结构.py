# Python 学习 1
# 2020/11/8 10:52

#简单的if else，双分支结果，单分支结构只有一个if
#a = 100
#b = int(input("输入一个数字"))
#if (a < b):
 #   print('失败')
#else:
 #   print('成功')

#多分支结构
def bijiao():
  a = int(input('输入一个数'))
  b = int(input('输入另一个数'))
  c = 50

  if(a > b and a > c):
    print('a>b')
  elif(a == b and a == c ):
    print('a==b')
  elif(a < b and a <c):
    print('a<b')
#python比较秀的地方
  elif(a<c<b):
    print('结束')
  elif(100>a>b):
    print('失败')
bijiao()
if(bijiao() != '失败'):
    print('结束')
