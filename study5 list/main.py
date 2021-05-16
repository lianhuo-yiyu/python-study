#python的列表 list 相当于数组  列表中括号[]
#列表创建
lst = ['hello', 100, 'hello', 100, 500, 4, 5]

lst1 = list([98, 46, 45])
print(lst1)
print(lst)
#list不同于数组在于索引从左数是0，1，2，3  还可以从右边数是-1，-2，-3  列表里面的数据类型可以不一样
print(lst1[1])
print(lst1[-2])

#index()获取list中的指定元素的索引位置
print(lst.index('hello'))  #存在相同元素只返回第一个的索引
print('100的第一个索引位置为'+str(lst.index(100)))
#在指定的LIST范围里查找指定元素的索引
#print(lst.index(500,0,4))  指定的位置左开右闭
print(lst.index(500,0,6))

#根据索引获得单个元素
lst2 = ['hello', 'das', 45, 78, 8, 85646, 50, 6, 456, 78]
print(lst2[5])
print(lst2[-1])

#获取list中的多个元素 需要进行切片的操作 列表名[start:stop::step]   切片的结果是原列表片段的一个拷贝 start默认0开始，stop省略默认到N-1，即最后， step默认为1 stop数的时候包含自己，但依旧是左闭右闭
lst3 = lst2[1:4:1]
print(lst3)
print(lst2[1:8:2])
print(lst2)
#step为-
print(lst2[::-1]) #负数step为倒序输出
print(lst2[::-3])

#判断元素是否存在于list
print(45 in lst2)
print('das' not in lst2 )

#列表元素的遍历
lst4 = [1, 2, 2, 456, 45, 100]
for i in lst4:
 #   print(i , end= '\t')
 print(i)

 #列表的增删改
#列表末尾添加一个元素 append
lst4.append(99)
print(lst4[-1::-3])
#列表末尾添加至少一个，多个元素
lst4.append(lst2)
print(lst4)
lst4.extend(lst2)
print(lst4)
print(lst4[7])
#列表任意一个位置添加一个元素 insert
lst4.insert(0, 3.1415)
print(lst4)
#任意位置添加多个元素 切片
lst4[1::1] = lst
print(lst4)
#列表元素的删除 remove 删除遇到的第一个元素
lst5 = [10, 20, 30, 40, 50, 60, 10, 20, 30, 46, 798, 9, 8, 7, 4, 56]
lst5.remove(20)
print(lst5)
#pop 根据索引进行元素的删除 同样只能单独移除 不指定删除索引默认删除最后一个元素
lst5.pop(0)
print(lst5)
#多个删除还是切片 删除至少一个元素
a = lst5[1:5]
print(a)
lst5 = lst5[1:5]
print(lst5)
#清空列表
lst5.clear()
print(lst5)
#del直接把这个lst5删除，相当于释放了其内存空间
#del lst5
#print(lst5)


#列表生成式
lst6 = [i for i in range(6)]
print(lst6)