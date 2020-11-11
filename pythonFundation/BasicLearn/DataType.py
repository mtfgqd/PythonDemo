# 字符串 字符串是以单引号'或双引号"括起来的任意文本
# 如果字符串内部既包含'又包含" 可以用转义字符\来标识
string = 'I\'m \"OK\"!'
print(string)

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m ok.')
print('I\'m learning\nPython.')

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

# 多行字符串'''...'''还可以在前面加上r使用,\n不会转义成回车换行
print(r'''hello,\n
world''')

# 尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，
# 在Python中，可以直接用True、False表示布尔值（请注意大小写）。布尔值可以用and、or和not运算
print(True)
print(False)
print(True and True)
print(True or False)
print(not False)

# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

# 变量
# 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头，
# 等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 123  # a是整数
print(a)
a = 'ABC'  # a变为字符串
print(a)
# Python变量不需要指定变量类型，变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
# 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。


# 常量
# 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
# 但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，
# 所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
PI = 3.14159265359


# 除法
# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数

print(10 / 3)  # 除法 3.33。。
print(10 // 3)  # 地板除 3
print(10 % 3)  # 取余 1