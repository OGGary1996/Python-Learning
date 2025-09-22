# 转换为整数int
# 字符串str-->整数int
# 纯数字的字符串
s = '2024'
n = int(s)
print("Type of s: %s, type of n: %s"%(type(s),type(n)))
# 浮点数float-->整数int
s1 = 2.23
print("s1 = %f"%s1)
print("s1 will be converted to int: %d"%int(s1))
# 布尔bool-->整数int
s2, s3 = True, False
print("s2 = %s, s3 = %s"%(s2,s3))
print("s2 and s3 will be converted to int: %d, %d"%(int(s2),int(s3)))

print("*" * 20)

# 转换为浮点数float
# str-->float
s = '324.6' # 有没有小数点都可以
print("s = %s"%s)
print("s will be converted to float: %f"%float(s))
# int-->float
n = 2024
print("n = %d"%n)
print("n will be converted to float: %f"%float(n))
# bool-->float
print("s2 = %s, s3 = %s"%(s2,s3))
print("s2 and s3 will be converted to float: %f, %f"%(float(s2),float(s3)))

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
print("n is a int, n = %d, after converted to str, n = %s, so now the type of n is %s"%(n,str(n),type(str(n))))
# float -->str
f = 5.3
print("f is a float, f = %f, after converted to str, f = %s, so now the type of f is %s"%(f,str(f),type(str(f))))
# bool --> str
a = True
print("a is a bool, a = %s, after converted to str, a = %s, so now the type of a is %s"%(a,str(a),type(str(a))))

# 进制的转换
s = '1a'
print("s is a string, s = %s, after converted to in with pase 16, s = %d"%(s,int(s,16)))