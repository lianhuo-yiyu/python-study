# Python 学习 1
# 2020/11/26 20:03
s = 'hello python hhh'
#字符串的替换 使用.replace()，第一个参数是待替换字符，第二个是替换的字符        第三个参数是最大替换字数，也就是要替换多少个相同的字串
print(s.replace('hhh', 'noway'))
s1 = 'hello python hhh hello python hhh hello python hhh hello python hhh'
print(s1.replace('hhh', 'nonono', 2))
#字符串的合并 只能合并列表元组中的字符串，或者是字符串本身的合并
print(s.join(s1))
lst = ['1', '6356+', 'j']
print('*'.join(lst))
yuanzu = ('dsa', 'ds', 'ad')
print("\\".join(yuanzu))