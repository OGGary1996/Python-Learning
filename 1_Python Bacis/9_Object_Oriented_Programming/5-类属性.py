# Python 中的属性分为2类：实例属性与类属性
# 1. 实例属性：属于具体对象，每一个对象可以不一样
# 2. 类属性：属于类本身，所有对象共享；类似于 Java 的静态成员变量


# 类属性 Class Attribute
# 1. 类属性属于类本身，被所有对象共享
class Student:
    school = "ABC College"
    def __init__(self, name):
        self.name = name

s1 = Student("Tom")
s2 = Student("Jerry")
print(s1.school)
print(s2.school)
print(Student.school)
# 这里的 school 写在类里面、方法外面，所以它是类属性。
# s1 和 s2 自己身上没有 school，但是它们都可以通过类访问到共享的 school。

# 2. 类属性适合保存对象共享的数据
# 比如：
class School:
    count = 0
    def __init__(self, name):
        self.name = name
        School.count += 1

s1 = School("ABC")
s2 = School("XYZ")
print(School.count)
# 这里每一次创建对象调用 __init__ 都会给类属性+1


# Python 和 Java 对比
# Java 中通常使用 static 关键字来表示静态变量
# public class Student {
#     public static String school = "ABC College";
# }


# 实例属性和类属性的访问顺序
# Python 访问属性时会先找对象，再找类
# 1. 先找 s1 对象自己有没有 school
# 2. 如果 s1 自己没有，再去 Student 类里面找 school
# 3. 如果类里面也没有，再去父类里面找
# 4. 都找不到才报错
class Student:
    school = "ABC College"

    def __init__(self, name):
        self.name = name

s1 = Student("Tom")
print(s1.name)
# 1. 先找 s1 对象自己
# 2. 找到了 name 属性
print(s1.school)
# 1. 先找 s1 对象自己
# 2. 没有 school
# 3. 再去 Student 类里面找
# 4. 找到了 school = "ABC College"


# 实例属性遮蔽类属性
# 1. 什么是遮蔽：对象中出现了和 类属性同名 的实例属性，导致通过对象访问时优先看到对象自己的属性。
class Student:
    school = "ABC College"

s1 = Student()
s2 = Student()

s1.school = "XYZ College"

print(s1.school)
print(s2.school)
print(Student.school)
# - s1.school：
# 	- s1 自己有 school，所以用 s1 自己的
# - s2.school：
# 	- s2 自己没有 school，所以去类里找
# - Student.school：
# 	- 直接访问类属性

# 2. 遮蔽不等于修改类属性
# 非常重要：s1.school = "XYZ College" 并不等于直接修改了类属性，而是直接给 s1 对象新增了一个同名的实例属性
# 所以 print(Student.school) 结果仍然是 "ABC College"

# 3. 正确修改类属性
# 可以通过 类名.类属性 进行修改，或者通过类方法进行修改
class Student:
    school = "ABC College"


s1 = Student()
s2 = Student()

Student.school = "XYZ College"

print(s1.school)
print(s2.school)
print(Student.school)


# 当类属性为可变对象时
class Student:
    hobbies = []

    def __init__(self, name):
        self.name = name


s1 = Student("Tom")
s2 = Student("Jerry")

s1.hobbies.append("reading")

print(s1.hobbies)
print(s2.hobbies)
print(Student.hobbies)
# s1.hobbies.append("reading") 修改的是这个共享列表本身，而不是新增一个同名的实例属性。


# 类内部和外部访问和修改类属性
# 1. 类内部和外部访问类属性都建议使用 类名.类属性
# 2. 类外部修改类属性可以使用 类名.类属性 或者类方法进行修改


# 完整示例
class Student:
    school = "ABC College"
    count = 0

    def __init__(self, name, score):
        self.name = name,
        self.score = score
        # 修改类属性
        Student.count += 1

    def introduce(self):
        print(f"Hello, I am {self.name}, I am from {Student.school}.")
    def show_score(self):
        return self.score

s1 = Student("Tom", 90)
s2 = Student("Jerry", 85)
s1.introduce()
s2.introduce()
print(s1.show_score())
print(s2.show_score())
print(Student.school)
print(Student.count)
