pi = 3.1415927

# 1. type()函数：用于查看变量的数据类型，传递参数为需要查看的变量，返回数据类型 type
# 2. isinstance()函数：用于判断变量是否是指定的数据类型，传递参数为变量和数据类型，返回True或False
#    数据类型：int, float, str, bool, list, tuple, dict, set
# 3. 与 java 中的 instanceof 关键字类似:
#    if (obj instanceof String) {...}

print("The type of variable pi is: ", type(pi))
print("The result of type() function is: ", type(type(pi)))

print("Is variable pi a string? -> ", isinstance(pi, str))
