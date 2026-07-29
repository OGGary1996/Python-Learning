# 浮点数的计算
n1 = 2.1
n2 = 15.256
print(n1 + n2)

# # 四舍五入round
# n3 =round(n1+n2, 2)
# print(n3)
#
# import math
# # 向上取整 ceil
# n4 = math.ceil(n1+n2)
# print("向上取整的结果是", n4)
# # 向下取整 floor
# n5 = math.floor(n1+n2)
# print("向下取整的结果是", n5)

# round()函数：输入参数为数值类型的变量和保留的小数位数，返回值为四舍五入后的结果。
n3 = round(n1 + n2, 2)
print(n3)

# mathy包 包含了一系列数学函数和常量，使用前需要导入math包。
import math
# 向上取整 ceil
n4 = math.ceil(n3)
print("n3 after ceil round is %d" %n4)
# 向下取整 floor
n5 = math.floor(n3)
print("n3 after floor round is %d" %n5)
