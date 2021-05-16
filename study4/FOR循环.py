# Python 学习 1
# 2020/11/9 10:09
for item in 'python':
    print(item)

#1到100的偶数和
sum = 0
for i in range(0,101,2):
    sum+=i
print(sum)
for a in range(3):
    b = int(input('输入一个数'))
    if b == 66:
        print('正确')
        break
    else:
        print('错误')
else:
    print('没机会了55')