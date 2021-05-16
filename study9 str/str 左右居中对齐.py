# Python 学习 1
# 2020/11/26 15:04
#center(x,y)居中对齐，第一个参数指定宽度，第二个参数指定填充字符（默认为空格）
s = 'hello, python,maybe I can USE YOU'
print(s)
#s = s.center(200)
print(s)

s = s.center(50,'*')
print(s)

#ljust()左对齐，第一个宽度，第二个填充字符 左对齐填充在右边，一直填够指定的宽度
s = s.ljust(100,'1')
print(s)

#rjust右对齐 一样 每一次对齐加入的填充字符变成了str的内容
s = s.rjust(200,'0')
print(s)


