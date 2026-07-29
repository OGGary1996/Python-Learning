# 常见编程思想
# 1. 面向过程编程：按照业务逻辑需要的实际步骤来完成
# 比如煮咖啡的过程
def boil_water():
    print("Boiling water")
def grind_beans():
    print("Grinding beans")
def brew_coffee():
    print("Brewing coffee")
boil_water()
grind_beans()
brew_coffee()
# 比如计算平均分的过程
scores = [70, 80, 90, 60]
total = sum(scores)
average = total / len(scores)
print(average)
# Java 中也可以使用面向过程编程，直接在 main 方法中调用静态方法即可

# 2.面向对象
# 面向对象的核心是：把现实世界中的事物抽象成对象，让对象自己管理自己的数据和行为。
# 面向对象的核心概念是 属性 + 方法
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

stu = Student("Alice", [90, 85, 95, 70])
print(stu.get_average_score())
# Student 对象
# ├── 数据：name, scores
# └── 行为：average_score()
# Java 的代码风格不一样：
# - Java 的一切都基于类，所有代码均写在某个类中
# - Java 类的类型是静态类型，而python为动态类型
# - 使用 private/protected 控制权限，而Python中使用命名约定比如 _name, __name
# - 对于接口，java 严格使用 interface 关键字，而Python为鸭子类型，注重行为本身，而不是抽象接口

# 3. 面向接口编程
# 核心是：不依赖具体实现，而是以来一套约定好的能力
# 在 Java 中非常常见，依赖的是接口本身的抽象能力，而不关心具体实现类的实现细节
# 在 Python 中没有强制性的 interface 关键字，但是也有接口的相关思想：
# 类似 Java 定义类
class CreditCard:
    def pay(self, amount):
        print(f"Paying {amount} using credit card")
class Cash:
    def pay(self, amount):
        print(f"Paying {amount} using cash")
# 模拟调用过程
def checkout(payment_method, amount):
    payment_method.pay(amount)
checkout(CreditCard(), 100)
# Python 中的接口思想是鸭子类型，也就是不管具体是什么类，主要具备相关的方法就行

# 4. 面向函数编程
# 核心是：把函数当作一等公民，用函数处理数据，减少状态变化
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x : x ** 2, numbers))
print(result)
# 也可以写成函数形式
def apply_operation(operation, obj):
    return [operation(x) for x in obj]


# 面向对象和核心思想：
# 1. 面向对象不是只创建 class
# 比如如下代码，虽然创建了 class 但是不符合面向对象的概念
# 这里 Student 只是一个装数据的壳，真正的逻辑仍然散落在外面。
class Student:
    pass
stu = Student()
stu.name = "Alice"
stu.math = 90
stu.english = 85
stu.science = 95
average = (stu.math + stu.english + stu.science) / 3
print(average)
# 更好的写法是：
class Student:
    def __init__(self, name, math, english, science):
        self.name = name
        self.math = math
        self.english = english
        self.science = science

    def get_average(self):
        return (self.math + self.english + self.science) / 3

stu_2 = Student("Alice", 90, 85, 95)
print(stu_2.get_average())

# 2. 面向对象的本质：对象 = 数据 + 行为
# Car 对象
# ├── 属性
# │   ├── brand
# │   ├── color
# │   └── speed
# └── 方法
#     ├── start()
#     ├── brake()
#     └── accelerate()
class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"Starting {self.brand} {self.color} car")
    def brake(self):
        print(f"Braking {self.brand} {self.color} car")

# 3.类和对象的关系
# 类是模板，对象是根据模板创建出来的具体实例。
# - 类 Class：设计图纸
# - 对象 Object：根据图纸造出来的具体东西

# 4. Python 中一切皆对象
# int float string list tuple dict set
# 但是 Java 中的基本数据类型不是对象