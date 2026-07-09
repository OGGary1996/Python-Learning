age = input('请输入你的年龄：')
# isdigit()函数用于判断input的输入的string是否为digital
if age.isdigit() :
    if 1 <= int(age) <= 120 :
        print('合法')
else :
    print('非法输入')
