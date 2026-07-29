# 函数的参数类型：
# 1. 位置参数:
# 依照顺序定义函数的形参，在调用时，必须依照顺序传递形参
def add(num1, num2):
    return num1 + num2
a, b = 3, 5
print(add(a, b))

# 2. 关键字参数
# 关键字参数是调用函数时，通过写出形参的名称与实参进行绑定，不依赖顺序的方式
def introduction(name, age):
    print(f'My name is {name}, I am {age} years old.')
# 可以改变顺序，但是必须要绑定
introduction(age=30, name = 'Tom')
# 在传递多参数时更加清晰：
def connect(ip, port, user, password):
    print(f'Connecting to {ip}:{port} as user {user} with password {password}.')
connect(
    ip = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '*****'
)
# !关键字参数必须放在普通参数之后,因为一旦涉及到多个参数，如果顺序混乱，且没有绑定关键字，则
introduction('Tom', age = 30) # 正确
# introduction(age = 30, 'Tom') # 错误

# 3. 默认参数
# 在函数定义时，就给形参一个默认值
# 如果传递了形参，那么会被覆盖；没有传递形参则使用默认值
def greet_with_default(user_name = 'Tom'):
    print('Hello, ' + user_name)
greet_with_default()
# 通常表示默认的配置，或者可选参数；
# 默认参数必须放在普通位置形参之后
def create_user(user_name, role='User'):
    print(f'User {user_name} successfully created with role {role}.')
create_user('Tom')
create_user('Jerry', 'Admin')
# 错误写法：
# def create_user(role='User', user_name):
#     print(f'User {user_name} successfully created with role {role}.')
# 默认值如果是可变对象比如list，可能产生其他效果
def add_item(item, items=[]):
    items.append(item)
    return items
print(add_item('apple')) # ['apple']
print(add_item('banana')) # ['apple', 'banana']
# 更加安全的写法是：
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
# 因为items是可变对象，所以每次调用都会产生新的对象

# 4. 可变参数
# 如果不知道最终需要传递几个参数，可以使用可变参数
def add_items(*item, items=None):
    if items is None:
        items = []
    items.append(item) # 以元组的形式加入所有的可变参数
fruits = ['kiwi', 'pear']
add_items('apple', 'banana', 'orange', items = fruits)
print(fruits)
# 关键字参数的可变参数
# 所有的实参和形参以dict的形式传递，形参名为关键字参数名
def show_info(**info) :
    print(info)
show_info(name = 'Tom', age = 30, gender = 'Male')

# 5. 同时使用各种类型的参数
# 常见的参数传递顺序：普通参数 -> *参数 -> 默认参数 -> **参数
def create_order(user, *item, coupon = None, **info):
    print(f'{user} ordered {item} with coupon {coupon} and additional info {info}')
create_order(
    'Tom',
    'Apple', 'Banana', 'Kiwi',
    coupon = '123456',
    address = 'Beijing',
    phone = '13800000000'
)


# 返回值
# 1. 单个返回值
def quare(num):
    return num ** 2
    print('This line will not be executed')
print(quare(3))
# return 会提前结束函数
def is_prime(num):
    if type(num) != int or num < 2:
        return None
    for i in range(2, num):
        if num % i == 0:
            return False
    return True # 注意不能将这个写在循环内部，

# 2. 返回多个值
# 此时实际上返回的是一个 tuple 元组
def get_max_min(num1, num2):
    return max(num1, num2), min(num1, num2)
    # return (max(num1, num2), min(num1, num2))
print(get_max_min(3, 5))
# 可以整体接收，也可以拆包接收
result = get_max_min(3, 5)
max_num, min_num = get_max_min(3, 5)

# 3. 无返回值
# Python没有 void 关键字，
# 如果没有写 return，则函数执行完毕后，会自动返回 None
# 可以显式声明 return 或者 return None