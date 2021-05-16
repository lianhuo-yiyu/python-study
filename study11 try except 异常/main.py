#try except  try内部是要进行的全部的代码，except后面输入异常，一般有个except baseexception（所有可能出现的异常）
# try except else
'''try:
    a = int(input('输入一个数'))
    b = int(input('输入拎一个'))
    res = a / b
#except BaseException:
 #   print('hhh,wrong')
except BaseException as e:
    print(e)
else:
    print('结果为', res)'''
# try except else finally
# finally不管出错与否都会运行，成功运行try else finally，出错运行try except finally

try:
    a = int(input('输入一个数'))
    b = int(input('输入拎一个'))
    res = a / b
except BaseException:
    print('hhh,wrong')
#except BaseException as e:
 #   print(e)
else:
    print('结果为', res)
finally:
    print('持之以恒')