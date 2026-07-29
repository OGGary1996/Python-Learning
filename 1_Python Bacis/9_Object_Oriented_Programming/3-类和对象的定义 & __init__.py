# 类与对象的区别
# 类可以理解为：一种模板、一张设计图、一种抽象出来的类型；具有一些共同特征
# 由类而构建的不同的实例，同一个类可以构建不同的多个实例对象


# 类的定义和创建
# 1. 创建一个最简单的类
class Student:
    pass

# 2. 根据定义好的类创建一个实例对象
# 调用类 Student() ↓
# Python 创建一个新的对象 ↓
# 把这个对象返回给变量 student
stu = Student()

# 3. 给对象添加属性
# 在 Python 中，可以通过直接给对象添加属性
# 但是，这种写法非常混乱，可能每个对象的属性名称并不一致，难以维护，所以不推荐
stu.name = 'Tom'
stu.age = 20
stu.gender = 'Male'
print(f"Student's name is {stu.name}, age is {stu.age}, gender is {stu.gender}.")

# 4. 创建带有初始化方法的类（ __init__ 方法 )
class Student:
    # 这里的 __init__ 方法是特殊的方法，用于在对象创建时自动调用 __init__,然后把属性保存到对象内部：
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print(f"Student's name is {self.name}, age is {self.age}, score is {self.score}.")

stu = Student("Tom", 29, 90)
stu.show_info()

# 5. 与 Java 的对比：
# - Java 的类可以有 public private 等等关键字做权限控制，但 Python 没有
# - Java 中使用 Constructor 构造方法来初始化属性，Python 中使用 __init__
# - Java 中的当前对象使用 this 关键字并且可以隐式声明，Python 中必须显式声明 self
# - Java 中必须要先声明属性变量，Python 中不需要


# __init__ 的底层理解
# 1. __init__ 是 Python 中的初始化方法，它会在对象创建之后自动执行。
class Demo:
    def __init__(self):
        print("Object initialized.")

obj = Demo()
# 这里我们并没有手动调用 __init__ 方法，在构建对象时，类的 __init__ 方法会自动执行

# 2. __init__ 的作用：给新创建的对象初始化属性赋值
# 执行的过程类似于：
#   1. Python 先创建一个空的 Student 对象
#   2. Python 将这个空对象传递给 __init__ 中的 self
#   3. __init__ 方法被调用，空对象中的属性被初始化
#   4. 将 stu 变量指向这个实例对象

# 3. __init__ 并不是构造函数
# __new__ 方法先执行，创建对象
# __init__ 方法后执行，给对象赋值

# 4. __init__ 方法不能指定返回值
# __init__ 方法的返回值默认为 None，不能指定返回其他值，否则会报错


# 完整案例：定义学生类并调用对象行为
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print(f"Student's name is {self.name}, age is {self.age}, score is {self.score}.")

    def is_passed(self):
        return self.score >= 60

stu_1 = Student("Tom", 29, 90)
stu_2 = Student("Jerry", 28, 55)
stu_1.show_info()
print(stu_1.is_passed())
stu_2.show_info()
print(stu_2.is_passed())

