# 1. break: 终止循环，注意：如果是嵌套循环，那么break只影响当前层面的循环
# 2. continue: 跳过当前循环，开始下一轮
# 3. else: 循环正常结束，但没有break时执行
# 4. java中没有循环+else体系，在判断时，需要搭配flag变量作为标识符使用

for i in range(10):
    if i>0 and i%3==0:
        print(i)
        break


while True:
    name = input("Please enter your name:")
    if name == 'ke' or name == 'Ke' or name == 'KE':
        print('welcome Ke!')
        break # 条件命中，此时终止整个while循环，后续代码都不会执行
    else: # 由于break终止了循环，此时break后面的else不会执行
        print('Wrong name, please try again!')


# 判断质数
# 质数：只能被1和自身整除的数，注意：1和0本身不是质数
# 判断一个数是否为质数
number = int(input('Enter a number:'))
for i in range(2, number): # 2~number-1
    if number % i == 0: # 如果number能被2~number-1的任意一个数整除，则不是质数
        print('%d is not a prime number' %number)
        break
else: # 使用 else 可以避免使用flag，因为else只会在break没有触发时才执行
    print('%d is a prime number' %number)
# 不使用else
number = int(input('Enter a number:'))
flag = True
for i in range(2, number): # 2~number-1
    if number % i == 0: # 如果number能被2~number-1的任意一个数整除，则不是质数
        print('%d is not a prime number' %number)
        flag = False
        break
if flag:
    print('%d is a prime number' %number)


# 输出 2-100 之间的质数
border = 100
number = 2 # 质数的最小值
while number < border:
    for i in range(2, number): # 2~number-1
        if number % i == 0: # 如果当前number能被2到number-1的任意一个数整除，则不是质数
            break # 终止当前的内层for循环
    else:
        print(number)
    number += 1
