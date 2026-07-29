# 函数的定义
# 函数是实现特定功能的、可重复调用的代码块。
# 它可以接收输入（参数），执行操作后返回结果（返回值）
# 不需要声明参数类型，返回值类型，可独立存在
def greet(user_name):
    print("Hello, " + user_name)
username = input("Please enter your name: ")
greet(username)

# 与Java的对比：
# 1. 必须声明参数类型，返回值类型
# 2. Java中方法是类中的一个函数，而Python中的函数是独立的函数，可以被任何对象调用。


# 文档字符串 Docstring
# 用于描述函数的功能，可以写在函数前面，也可以写在函数后面
def greet(user_name):
    """
    This is a greeting function.
    :param user_name: The name of the user.
    :return: None
    """
    print("Hello, " + user_name)