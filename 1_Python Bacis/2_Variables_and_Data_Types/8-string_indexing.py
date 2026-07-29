# 创建字符串
s = 'hello,world'

# 取出string中某一个字符
# 变量名[索引]
# 注意：
#   1. 索引从0开始
#   2. 索引可以为负数，-1表示最后一个字符， -2表示倒数第二个字符，以此类推
print("First char in s: ", s[0])
print("Second char in s: ", s[1])

# 取出string中的多个字符
# 变量名[起始索引:结束索引+1:步数]
# 注意：
#   1. 左闭右开，不包含结束索引，所以需要+1
#   2. 步长默认为1，可以不写
#   3. 起始索引为0，可以省略
#   4. 结束索引为-1，可以省略,省略之后就包含最后一个索引，不省略则遵守左闭右开的规则
print("First 3 chars in s: ", s[:3:])
print("Final 2 chars (final included) in s:", s[-3:-1:])
print("Final 3 chars in s: ", s[-3::])
print("Final 3 chars in s: ", s[-3:len(s):])

# 反转字符串
print("After reverse: ", s[::-1])
