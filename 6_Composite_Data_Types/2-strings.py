# 字符串的基本特性
# Python 中使用单引号''或者双引号""，三引号实现多行字符串""" """
# Java 中只能使用双引号""表示字符串，单引号''则表示单个字符。
# 但是 Python 中没有单个字符这个说法，单个字符仍然表示一个完整的字符串。
from distutils.command.install import key

a = 'Hello'
b = "World"
c = """多行
字符串"""
char = 'A'
print("Type of char is: ", type(char))

# 字符串的不可变性：任何修改操作都会形成一个新的字符串对象，而原来的那个不受影响。
# Java 中也是一样，Java 中的 String 也是不可变对象。两者在内部都有字符串驻留机制，用于节省内存。
s = "hello"
s.upper()
print(s) # 仍然是hello

# 字符串的索引
# 字符串可以像序列一样通过索引访问。
# 索引从 0开始，支持负索引（-1表示倒数第1, -2表示倒数第2，以此类推）。
s = "hello, world!"
print(s[0])
print(s[-2])
# 切片
# Java的对应方法 s.subString(index1, index2)
print(s[0:5])
print(s[7:-1])
print(s[::-1]) # 反转

# 字符串的常用方法
# 大小写转换
# 对应Java中的 s.toUpperCase()/s.toLowerCase()
print(s.upper()) # 转换为大写
print(s.lower()) # 转换为小写
print(s.capitalize()) # 首字母大写

# 查找和替换
print(s.find('hello')) # 查找第一个hello的位置
s_replaced = s.replace('!', '.') # 注意，修改操作会返回新的字符串，原字符串不受影响
print(s_replaced)
print(s)

# 分割 str -> list
# 返回新的字符串列表，原始字符串不受影响
# 对应Java中的 String[] fruits = s.split(",")
s_fruits = 'apple,orange,banana'
fruits = s.split(',') # 以 ',' 作为标识符分割
print(fruits, ", type: ", type(fruits))
print(s)
# 拼接 list -> str
# 直接使用 + ，但是在循环中拼接会造成性能损耗，建议使用 join 方法，类似于java中的 StringBuilder
# 对应Java中的 String joined = String.join("-", fruits)
joined = '-'.join(fruits) # 以 '-' 作为拼接符号进行拼接list，返回一个新的字符串
print(joined, ", type: ", type(joined))

# strip去掉空格
# 返回修改后的新的字符串
# 对应java中的 s_spaces.trim()
s_spaces = '  Hello  '
print(s_spaces.strip()) # 去掉两边的空格
print(s_spaces.lstrip()) # 去掉左边的空格
print(s_spaces.rstrip()) # 去掉右边的空格
print(s_spaces)

# 判断类型
print('123'.isdigit()) # 判断是否为数字,True
print('abc'.isalpha()) # 判断是否为字母,True
print('abc123!'.isalnum()) # 判断是否为字母数字,False
print('Hello'.istitle()) # 判断是否为首字母大写,True

# 格式化输出
# 1. f-string,推荐使用
# 2. .format()方法
# 3. 旧 % 格式
name = 'ke'
age = 30
print(f'My name is {name}, I am {age} years old.')
print('My name is {}, I am {} years old.'.format(name, age))
print('My name is %s, I am %d years old.' %(name, age))

# 字符串的遍历
for char in s:
    print(char)
# 相当于Java中的增强for，但是String不能直接遍历，需要转换为char数组
# for (char c : s.toCharArray()) {...}

# 成员判断
# in / not in
print('a' in s)
print('A' in s)
print('A' not in s)
# 相当于Java中的 s.contains("...")