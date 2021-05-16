#函数的原理与利用
#函数的创建
#def 函数名([输入参数]):
 #   函数体
  #  [return xxx]
def cale(a,b):
  #  c = a + b
    c = a - b
    return c
result = cale(10,20)
print(result)

#函数调用时的参数传递    创建的时候函数括号里面是def hhh(形参，形参)，  在函数的调用处，括号里面的是实参，实际参数     形参和实参的名字可以不相同
#参数的传递（实参的值传给形参）
#1 位置实参   如上例，按存放的第一个第二个位置传递
#2 关键字传参，就是将形参自行按需求赋值
result2 = cale(b=20, a=33)
result3 = cale(b = -10, a = 33)
print(result2)
print(result3)

#在函数调用过程中，进行参数的传递。如果参数是不可变对象，在函数的中的修改值出了函数就会变回去，不会影响实参的值，如果是可变的对象，那么参数的改变会一直存在，函数调用过后值也是被修改过的
def lit(a, b):
      b.append(30)
      a = list(a)
      print('函数里面的数据类型为',type(a))
      print(b)
a = 'python'
b = [10, 30, 50]
lit(a,b)
print(a)
print('函数外面的数据类型',type(a))
print(b)

#函数的返回值 return
#函数没有返回值   即函数调用过后，不用为调用该函数的函数提供出输入的数据
def fun():
    print('hhh')
fun()

#函数返回的只有一个返回值，也就是被调用的函数只做了一项运算有一个结果需要提供出去，return 结果，直接返回该结果的数据类型
def fun1():
    return 'hehehe'
res = fun1()
print(res)
print(fun1())  #整个函数就代表那一个数值

def fun2():
    return  'aa','bb' #返回多个数值，所有的返回值作为一个元组出现
res2 = fun2()
print(res2)
print(fun2())

