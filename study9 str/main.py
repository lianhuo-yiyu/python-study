#str的驻留机制   指相同的字符串只会占据一个内存空间，一个字符串只被创建一次，之后新的变量是获得之前的字符串的地址
a = 'python'
b = "python"
c = """python"""
print(id(a))
print(id(b))
print(id(c))

s1 = ''
s2 = ''
print(s1 == s2)
print(s1 is s2)
print(id(s1))
print(id(s2))

#理论上有特殊字符串不驻留，下面这个cmd不驻留，pycharm进行了优化
z1 = 'a%'
z2 = 'a%'
print(id(z1))
print(id(z2))