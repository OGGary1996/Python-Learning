weather = '晴天'
if weather == '下雨':
    print('出门要带伞') # 缩进
else:
    print('戴个帽子')

# 判断年龄
age = int(input('请输入你的年龄：'))
if age >= 18:
    print('可以去网吧')
else:
    print('在家写作业吧')

# 三元表达式简化表达
# 类似于Java的：
# String result = age >=18 ? "Can Access" : "Can't Access"
result = "Can Access" if age >=18 else "Can't Access"
print(result)
