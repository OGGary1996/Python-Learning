# 转换为整数int
# 字符串str-->整数int
# 纯数字的字符串
s = '2026'
n = int(s)
print("s: ", s, "type of s: ", type(s))
print("n: ", n, "type of n: ", type(n))

# 浮点数float-->整数int，此时向下取整，等于round()
n_2 = 3.14
n_3 = int(n_2)
print("n_2: ", n_2, "type of n_2: ", type(n_2))
print("n_2: ", n_3, "type of n_3: ", type(n_3))

# 布尔bool-->整数int
b_1, b_2 = True, False
n_4, n_5 = int(b_1), int(b_2)
print("b_1 & b_2 ", b_1, b_2, "type of b_1 & b_2: ", type(b_1))
print("n_4 & n_5 : ", n_4, n_5, "type of n_4 & n_5: ", type(n_5))

print("*" * 20)

# 转换为浮点数float
# str-->float
s_2 = '324.6' # 有没有小数点都可以
f_1 = float(s_2)
print("s_2: ", s_2, "type of s_2: ", type(s_2))
print("f_1: ", f_1, "type of f_1: ", type(f_1))

# int-->float
n_6 = 2026
f_2 = float(n_6)
print("n_6: ", n_6, "type of n_6: ", type(n_6))
print("f_2: ", f_2, "type of f_2: ", type(f_2))

# bool-->float
f_3 = float(b_1)
f_4 = float(b_2)
print("f_3 & f_4: ", f_3, f_4, "type of f_3 & f_4: ", type(f_4))

print('*'*20)

# 转换为布尔bool
# str-->bool
s = '0'
print("s is a string contain something, even though it's '0',s = %s"%s)
print("s will be converted to bool: %s"%bool(s))
s1 = ''  # 空串
print("s1 is an empty string, s1 = %s"%s1)
print("s1 will be converted to bool, s1 = %s"%s1)

# int-->bool
n=0
print("n is a number, n = %d"%n)
print("n will be converted to bool: %s"%bool(n))

# float-->bool
f=0.0
print("f is a float number, f = %f"%f)
print("f will be converted to bool: %s"%bool(f))

print("*"*20)

# 转换为字符串str
# int-->str
n = 5
print("n is a int, n = %d, after converted to str, n = %s, so now the type of n is %s" %(n,str(n),type(str(n))))

# float -->str
f = 5.3
print("f is a float, f = %f, after converted to str, f = %s, so now the type of f is %s" %(f,str(f),type(str(f))))

# bool --> str
a = True
print("a is a bool, a = %s, after converted to str, a = %s, so now the type of a is %s" %(a,str(a),type(str(a))))

# 进制的转换
s = '1a'
print("s is a string, s = %s, after converted to in with pase 16, s = %d" %(s,int(s,16)))