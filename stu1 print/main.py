#Python 学习 1
#${DATE} ${TIME}
print("helloworld")
print('helloworld')
print('hello','world')#输出到一行

fp = open('D:\\pycharm\\workspace\\study\\stu1 print\\text1.txt', 'a+')#输出到文件的格式
print('helloworld', file=fp)
fp.close()

print(3+1) #输出一个算式的值

print("'D:\\pycharm\\workspace\\study\\text1.txt")#不想让字符串被当做转义字符
print(r"D:\pycharm\work space\study")


