#字典 {   }    可变序列    dict     以键值对的方式存储数据  ｛name : hhh｝:前面的叫键，：后面的叫值   字典是无序的序列  字典存储是key时经过hash计算
#字典的键key不允许重复，只有值可以重复，后面的键值会覆盖相同的键名  列表可以按照自己的想法找地方插入元素，dict不行，它是无序的 字典空间换时间，内存浪费大
zidian = {'name' : 'python' , "nianling" : 24}
print(zidian)
c = dict(name = 'python', nian = 100)
print(type(c))
print(c)

#字典中的值获取
print(zidian['nianling'])
#print(zidian['nian'])

print(c.get('nian'))
print(c.get('nianling'))
print(c.get('nianling', 'bucunzai')) #可以让返回的none值变成不存在

#列表可以按位置插入
lst =[5,6,9,7,5,0,5]
lst.insert(1, -1)
print(lst)
