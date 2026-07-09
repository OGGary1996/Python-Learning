# 初始条件
n = 0
while n < 10:
    print(n)
    n += 1

# 高斯求和: 1+3+5+...+10000 = 50005000
n = 2
total = 0
while n <= 10000:
    total += n
    n += 2
print(total)


# 死循环，没有设置出口时永久循环
# while True :
#     print(1)

