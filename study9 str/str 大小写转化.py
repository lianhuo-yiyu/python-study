# Python 学习 1
# 2020/11/26 14:47
#总结 upper（）  lower()  swpcase()  capitalize()  title()
#upper 字符串中的字符都转为大写
s = 'python'
a = s.upper()
print(a)
print(id(s))
print(id(a))

#lower（）字符串中所有字符转化为小写
b = s.lower()
print(b)

#大写转小写，小写转大写
s1 = "hhh, I like PYTHON"
s2 = s1.swapcase()
print(s2)

#capitalize()字符串中第一个字符转大写，其余字符均小写
s3 = s1.capitalize()
print(s3)

#title（）字符串中每一个单词的第一个字符大写，其余部分都转化为小写】
s4 = s1.title()
print(s4)