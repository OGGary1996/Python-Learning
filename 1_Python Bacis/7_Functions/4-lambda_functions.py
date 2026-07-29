# Lambda 匿名函数
# Lambda 表达式用于创建匿名函数
# 1. 普通函数使用 def 创建，有名称
# 2. 匿名函数使用 Lambda 创建，没有名称，表示一次短小的简单的，一次性的计算逻辑

# lambda : 参数 : 表达式（返回值）
square = lambda x: x ** 2 # 表示接收一个 x，返回 x 的平方

# Lambda 本质上也是函数，只是写法更简洁，更短
# 但是在开发中如果业务逻辑比较复杂，通常使用 def 而不是强行使用 lambda
def add(x, y) :
    return x + y
add_lambda = lambda x, y: x + y
# 两者调用方式完全相同
print(add(3, 4))
print(add_lambda(3, 4))


# Lambda 的语法规则
# 1. Lambda 的函数体只能是一个表达式，不能写多行语句。
# 错误示范：
# square = lambda :
#   y = x ** 2
#   return y
# 在lambda中，y = x ** 2 和 return y 都是返回语句

# 2. 不需要写 return 返回值声明，表达式的结果自动作为返回值
is_even = lambda x : x % 2 == 0 # 不需要 if 语句和 return 语句
print(is_even(3))
print(is_even(4))

# 3.可以有多个参数，也可以没有参数
add_lambda = lambda *x : sum(x)
print(add_lambda(1,2,3,4,5))
greet = lambda : "Hello User"
print(greet())

# 主要使用场景是在操作集合类型时，对集合或者其中的元素做修改
# 1. 配合 sorted() 自动排序
# sorted() 中的参数 key 表示按照什么字段排序，这里传递每个元素中的年龄
# sorted() 函数的返回值是一个排序后的列表
employees = [
    ('Bob', 75),
    ('Adam', 92),
    ('Bart', 66),
    ('Lisa', 88)
]
emp_sorted = sorted(employees, key=lambda emp:emp[1])
print(emp_sorted)
emp_dict = dict(employees)
# 注意，sorted() 方法需要可排序的对象，不能直接使用emp_dict
emp_sorted_dict = sorted(emp_dict.items(), key=lambda emp:emp[1])
print(emp_sorted_dict)


# 2. 配合 map() 重新映射元素
# map() 函数表示会将可迭代对象中的每一个元素执行相同的逻辑，进行重新映射
# 注意：map() 的返回值是一个 map对象，需要使用list重新转换为list对象
num_list = [1,2,3,4,5]
num_list_square = list(map(lambda x : x **2, num_list))
print(num_list_square)
# 也可以更快的使用列表推导式
num_list_square_2 = [x ** 2 for x in num_list]
print(num_list_square_2)

# 3. 配合 filter() 函数来过滤集合元素
# filter() 函数表示会将可迭代对象中的每一个元素执行相同的逻辑，进行过滤
# 注意：filter() 的返回值是一个 filter 对象，需要使用list重新转换为list对象
num_list_filter = list(filter(lambda x : x % 2 == 0, num_list))
print(num_list_filter)
# 也可以更快的使用推导式
num_list_filter_2 = [x for x in num_list if x % 2 == 0]

# 4. 作为回调函数，将lambda作为对象传递到函数中
# 回调函数：在方法定义中，先使用占位符声明方法，在后续调用，传递lambda表达式
def calculate(a, b, operation):
    return operation(a, b)
result = calculate(3, 5, lambda x, y: x + y)
print(result)


# lambda 和条件表达式
# lambda 中不能使用多行 if 语句，但是可以使用条件表达式
max_num = lambda a, b : a if a > b else b
even_num = lambda x : 'True' if x % 2 == 0 else 'False'
print(max_num(3, 5))
print(even_num(3))

# lambda 的作用域
# lambda 可以读取当前作用域的变量
# 但是需要注意的是，读取的变量值为当前的变量值
factor = 10
multiply = lambda x : x * factor
factor = 100
print(multiply(3)) # 300，此时 factor 为100





