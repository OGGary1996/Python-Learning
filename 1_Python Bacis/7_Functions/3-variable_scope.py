# 1. 局部变量
def print_num():
    num = 10
    print(num)
print_num()
# print(num) 会报错，num 未定义

# 2. 全局变量
x = 10
def print_x():
    print(x)
print_x()
print(x)
# 函数内部可以直接读取全局变量，但是直接修改会有作用域问题
def change_x():
    x = 100 # 相当于重新定义了一个新的局部变量 x=100，并没有修改外部的全局变量 x
    print(x)
change_x()
print(x) # x 还是10

# 3. 修改全局变量（不推荐）
# 实际开发中尽量不使用，因为会使得函数依赖于外部的全局变量，降低复用性
def change_global_x():
    global x # 通过 global 关键字，表示 x 为全局变量 x
    x = 100
    print(x)
change_global_x()
# 推荐的方法是 函数内部仅仅定义通用修改方法，采用参数传递
def change_num(num):
    return num + 10
num = 10
num = change_num(num)
print(num)

# 4. 嵌套作用域
# 如果函数内部还存在嵌套的函数，那么内部函数可以访问外部函数的局部变量，称为 enclosing 作用域
def outer():
    message = 'Hello'
    def inner():
        print(message)
    inner()
outer() # Hello
# 如果需要修改外部函数的变量，通过 nonlocal 关键字
def counter():
    count = 0
    def add():
        nonlocal count # 获取到外部函数的局部变量
        count += 1
        return count
    return add
c = counter()
print(c()) # 1
print(c()) # 2