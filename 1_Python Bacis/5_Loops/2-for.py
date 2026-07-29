
# Python的索引循环
# 等价于Java的普通for循环：
# for (int i = 0, i < 100, i++) {...}
for i in range(10):
    print(i, end = '') # 控制不换行
print('')

# Python的迭代器循环
# 等价于java中的增强for
# for (int i : list) {...}
list_demo = [0,1,2,3,4,5,6,7,8,9]
for i in list_demo:
    print(i, end = '')
print('')

# 高斯求和
# 1. 使用 while 循环
n = 2
result_1 = 0
while n <= 100 :
    result_1 += n
    n += 2
print(result_1)
# 2. 使用 for 循环
result_2 = 0
for i in range(1,101) :
    if i % 2 == 0 :
        result_2 += i
print(result_2)

# 1!+2!+3!..+n!
# 1. 使用 while 循环
n = 1
result_3 = 0
while n <= 20 :
    result_temp = 1 # 临时存储阶乘结果，注意不能是0
    m = 1
    while m <= n :
        result_temp *= m
        m += 1
    result_3 += result_temp
    n += 1
print(result_3)
# 2. 使用 for 循环
result_4 = 0
for i in range(1,21) :
    result_temp = 1
    for j in range(1,i+1) :
        result_temp *= j
    result_4 += result_temp
print(result_4)

layer = 5
# 打印*矩阵
for i in range(layer) :
    for j in range(layer) :
        print('*',end='') # 控制不换行
    print() # 控制换行

# 打印*直角三角形
for i in range(layer) :
    for j in range(i+1) :
        print('*',end='')
    print()

# 打印*倒直角三角
for i in range(5) :
    for j in range(5-i) :
        print('*',end='')
    print()

# 打印*等腰三角形
for i in range(layer) :
    # 1. 先打印单侧空格，对于单侧，上一行比下一行多1个空格，单侧个数为layer-i
    for space in range(layer-i) :
        print(' ',end='')
    # 2. 再打印星号，每一层个数为i*2+1
    for star in range(i*2+1) :
        print('*',end='')
    print()

# 打印*倒等腰三角形
# 逆向*等腰三角形的外层循环
for i in range(layer-1, -1, -1) : # 从layer-1开始倒序，到0（包含）
    # 1. 先打印单侧空格，对于单侧，上一行比下一行多1个空格，单侧个数为layer-i
    for space in range(layer-i) :
        print(' ',end='')
    # 2. 再打印星号，每一层个数为i*2+1
    for star in range(i*2+1) :
        print('*',end='')
    print()
# 正向逻辑
for i in range(layer) :
    # 1. 先打印空格，对于单侧，上一行比下一行少1个空格，单侧个数为i
    for space in range(i) :
        print(' ',end='')
    # 2. 再打印星号，每一层个数是2*(layer-i)-1
    for star in range(2*(layer-i)-1) :
        print('*',end='')
    print()