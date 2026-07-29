# match 语句：
# 用于简单的等值对比，只能对比值是否相等，不能对比复杂的逻辑条件

x = input("Please enter a hello message: \n")
match x :
    case "hello" :
        print("Message Correct")
    case "helo" :
        print("Message Correct, a 'l' was missing")
    case "hllo" :
        print("Message Correct, a 'e' was missing")
    case _ :
        print("Message Incorrect")
