# is 和 == 的区别：
# 在java中：
#   1. .equals() 表示比较对象的内容，如果内容相同，则返回true
#   2. == 表示比较对象引用，如果对象引用的同一个，则返回true
#   3. 注意：如果对象的内容或者值相同，但是并非同一个内存地址，则两者有区别
#   4. == 的比较程度更深
# 在python中：
#   1. is 相当于java中的 == 引用比较，需要内存地址相同
#   2. == 相当于java中的 .equals() 内容比较，需要内容相同
#   3. is 的比较程度更深

print(3 != 3)  # 判断不相等
print(3 == 2)  # 判断相等
print(3 >= 2)
print(3 <= 3)
print(3.0 == 3)
print(True == False)
print('hello' < 'hell')  # 字符串的比较运算：每个字符的ascii码值
print(1<2<3)
print(1<2 and 2<3)
print('y'<'x'==False)
print('y'<'x' and 'x'==False)
