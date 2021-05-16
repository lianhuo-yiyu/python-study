#数据类型 集合 只有键没有值的字典
#集合的创建    集合中的元素不允许重复     set（）  集合中元素无序,如c
s = {1, 2, 5, 5, 4}
print(s)
a = set(range(11))
print(a)
print(type(a))
c = set('python')
print(c)

#集合的判断
print(2 in s)
#集合增加元素
a.add(88)
print(a)
c.update([10,20,30])
print(c)
#集合元素的删除
a.remove(5)
print(a)
a.discard(10)
print(a)
s.pop()
print(s)
s.clear()
print(s)
a.clear()
print(a)

#集合相等与否
print(a == s)
#集合是否有子集关系
a = {10, 20, 30, 50}
b = {10, 20, 30, 50, 70}
print(a == s)
print(a.issubset(s))
print(a.issubset(b))

#超集
print(a.issuperset(b))

#集合间是否有交集
print(a.isdisjoint(s))

#集合数学操作  交并补差
s1 = {10, 20, 30, 40}
s2 = {10, 11, 12, 13}
print(s1.intersection(s2) )#交
print(s1 & s2)#交集 = and

print(s1.union(s2))
print(s1 | s2)#并  = or

print(s1.difference(s2))#差
print(s1 - s2)#差集

#对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

#集合生成式 集合｛i+=i for i in range ()｝
hh = {i*2 for i in range(10)}
print(hh)
print(type(hh))