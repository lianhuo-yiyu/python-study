# Python 学习 1
# 2020/11/26 19:46
s = 'hello world python hhh'
#从左边分割（劈分），可以通过一个sep来说明是通过什么完成分割的，一般默认是空格        还可以加上一个maxsplit(分段的数目）来确认分作几段,从左边数够了之后剩下的都作为列表中的一个元素
lst = s.split()
print(lst)
print(type(lst))
s1 = 'hello|hi|python|hhh'
lst1 = s1.split(sep='|')
print(lst1)
lst2 = s1.split(sep='|', maxsplit=2)
print(lst2)

#从右边劈分，都一样 rsplit
lst3 = s.rsplit()
print(lst3)
lst4 = s1.rsplit(sep='|', maxsplit=2)
print(lst4)