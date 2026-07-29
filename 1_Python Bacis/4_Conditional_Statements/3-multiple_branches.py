# 在多条件if-elif判断中：
# if的执行逻辑是从上到下，逐行执行
# 所以不需要将多余的边界条件补充进去
# 比如 score >=90, 下一个条件不用：90 < score <= 80，而是：score >= 80

score = input("Please enter a score: \n")
score = int(score)
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else :
    print('D')


# bmi计算
# bmi =w/(h*h)
w = float(input('请输入你的体重，单位kg：'))
h = float(input('请输入你的身高，单位米：'))
bmi = w / (h * h)
print(bmi)
if bmi < 18.5:
    print('多吃一点才健康')
elif bmi < 23.9:
    print('你的体型非常的标准')
else:
    print('适当的可以多运动一下')
