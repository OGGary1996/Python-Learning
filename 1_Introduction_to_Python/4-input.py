# # 任务1
# name = input("请输入你的名字：")
# print(name)
#
# # 任务2
# age = input("请输入你的年龄：")
# # 类型转换
# age = int(age)
# # print(type(age))
# year = 2024
# # print(type(year))
# birth = year - age
# print("你的出生年份是", birth)

# input 函数表示接受一个输入参数
# 注意：接收的参数数据类型为 string 类型
name = input("Please enter your name: ")
age = input("Please enter your age: ")
# 类型转换
age = int(age)
print("User Name: %s, Age: %d" %(name, age))

year = 2026
print("User birth year: %d" %(year-age))
