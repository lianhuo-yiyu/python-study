# Python 学习 1
# 2020/11/26 20:25
#格式化字符串 也就是%d,%s等等
#字符串编码转化
#字符串转byte
s = 'hello world'
s1 = '十年一剑'
print(s1.encode(encoding='GBK'))
print(s.encode(encoding='UTF-8'))

#解码
a = s1.encode(encoding='GBK')
print(a.decode(encoding='GBK'))