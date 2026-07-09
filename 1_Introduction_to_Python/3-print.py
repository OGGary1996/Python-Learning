year = 2026
month = 7
day = 20
week = "--"
weather = "Sunny"
temp_cel = 31

# 1. sep 表示设置打印多个内容时的分隔符，
# 2. end 表示设置print执行结束后的操作, 这里 '\n' 表示换行
print("Today is ", year, month, day, sep = "-", end = "\n")

print("Today is %d year %02d month %d day, week %s, weather %s, temperature(Celsius) %.1f" %(year, month, day, week, weather, temp_cel))
