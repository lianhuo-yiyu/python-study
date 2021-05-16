# Python 学习 1
# 2020/11/5 15:28
# and, or , not    与，或，非    也就是and真真为真， or假假为假                   还有一个in 和 not in,进行遍历判断在与不在
a, b = 10, 20
print(a>0 and b>0)
print(a>9 and b<10)

print(a > b or b > 2)
print(a > 2 or b < 50)

f = 0
print(f) # 0的bool为false
print(not f)

i = 'python'
print('a' in i)
print('y' in i)
print('b' not in i)
