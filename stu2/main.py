#PYTHON study2
import keyword
#变量不用预先定义
a=('STUDY')
print(a)

#变量类型 int float bool string
a=454;
print(type(a))
print('默认输出的是十进制的数字', 0b100000111)
print('八进制是从1-7里面选数', 0o1544)
print('16进制', 0x1E2f)

#BOOL里面 TRUE是1 FLASE是0

a='python'
b=2020#这里的2020是int型，直接print时肯定会出现字符串和INT类型的冲突,print还是全部转化为str类型
b=str(b)
print('I like\t' + a + '\tsince\t' + b)
print('I like python since 2020')
print('abcdefghijklmnopqrstuvwxyz')



