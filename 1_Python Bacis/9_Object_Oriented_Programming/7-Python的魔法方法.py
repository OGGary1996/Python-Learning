# 什么是魔法方法
# 1. 魔法方法的基本概念
# Python 中有一类特殊方法，长这样：方法名前后都有两个下划线
# __init__
# __str__
# __repr__
# __len__
# __eq__
# __add__

# 2. 为什么叫“魔法方法”
# 这些方法通常不是我们手动直接调用的，而是在特定语法或内置函数触发时，由 Python 自动调用。
# 比如最重要的魔法方法 __init__()，在创建对象时，自动调用，为属性赋值


# 魔法方法的核心作用
# 1. 让自定义对象融入 Python 语法
# 比如 Python 内置列表可以这样用：
numbers = [1, 2, 3]
print(len(numbers)) # __len__()
print(numbers[0]) # __getitem__()
print(numbers + [4, 5]) # __add__()
# 如果我们自己定义类，也实现这些魔法方法，就可以让对象支持类似行为。

# 2. 对比 Java 的写法
# Java 中很多行为需要显式写方法：
# student.toString();
# student.equals(otherStudent);
# student.hashCode()
# student.compareTo(otherStudent)
# 对应 Python 中的 __str__(), __eq__(), __hash__(), __lt__()


# 最重要的魔法方法 __init__()
# 1. 我们之前已经很熟悉 __init__() 方法本质上就是魔法方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("Tom", 20)
# 2. 调用过程
# 在创建对象时，python 自动调用该方法，对属性赋值
# 创建空对象 -》 传递 self 给 __init__()  -》 调用 __init__()

# 3. 严格来说 __init__() 不是构造器，__new__() 才负责创建对象


# 对象字符串表示：__str__ 和 __repr__
# 1. 默认的打印对象的方法存在的问题：默认打印对象的类型和内存地址
print(s1) # <__main__.Student object at 0x104dc7f40>
# 但是我们更希望能看到对象的具体属性

# 2. 通过实现 __str__()，给用户看的字符串
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student's name is {self.name}, age is {self.age}."
s1 = Student("Tom", 20)
print(s1)

# 2. 通过实现 __repr__()，给开发环境看的字符串
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"
s1 = Student("Tom", 20)
print(s1)

# 3. __str__ 和 __repr__ 的区别:
# 如果只想让对象打印得更清楚，可以先写 __repr__
# 如果同时写 __str__ 和 __repr__ 此时优先调用 __str__


# 对象比较：__eq__
# 注意：
# 在java 中对象比较有2种方式：
#  - == 比较的是引用（内存地址）是否相同。对基本类型（int、double等）比较的是值本身。
#  - equals()：默认情况下（继承自 Object 类），equals() 的行为和 == 一样，也是比较内存地址。
#    - 但很多类（比如 String、Integer、自定义类）会 重写（override）这个方法，
#    - 使得 equals 方法用于比较值
# 在 Python 中也有2种方式：
#  - is 比较的是对象的身份（identity），也就是内存地址是否相同 —— 这个对应 Java 的 ==
#  - == ：默认（继承自 object）情况下等价于 is（比较地址）
#    - 但很多内置类型（如 str、list、dict）和自定义类都可以重写 __eq__() 来比较内容
#    - 这个对应 Java 的 equals

# 1. 默认对象比较的问题：比较内存地址，而不是比较属性
s1 = Student("Tom", 20)
s2 = Student("Tom", 20)
print(s1 == s2) # False

# 2. 使用 __eq__() 自定义比较规则
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
s1 = Student("Tom", 20)
s2 = Student("Tom", 20)
print(s1 == s2) # True

# 3. 更安全的写法，补充类型判断，保证只能比较同一类型
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.name == other.name and self.age == other.age
s1 = Student("Tom", 20)
s2 = {"name": "Tom", "age": 20}
print(s1 == s2) # False


# 对象长度：__len__
# 1. 列表可以这样访问
numbers = [1, 2, 3]
print(len(numbers)) # __len__()

# 2. 对自定义类型实现 __len__
class Classroom:
    def __init__(self, students):
        self.students = students
    def __len__(self):
        return len(self.students)
c1 = Classroom(["Tom", "Jerry", "Alice"])
print(len(c1)) # __len__()


# 对象索引访问：__getitem__
# 1. 列表可以这样访问
numbers = [1, 2, 3]
print(numbers[0]) # __getitem__()

# 2. 对自定义类实现 __getitem__
class Classroom:
    def __init__(self, students):
        self.students = students

    def __getitem__(self, index):
        return self.students[index]
c1 = Classroom(["Tom", "Jerry", "Alice"])
print(c1[1]) # __getitem__()

# 3. 也支持切片
print(c1[::-1]) # __getitem__()


# 对象可迭代：__iter__
# 1. 对列表可以这样访问
students = ["Tom", "Jerry", "Alice"]
for student in students:
    print(student)

# 2. 对自定义类型实现 __itr__
class Classroom:
    def __init__(self, students):
        self.students = students
    def __iter__(self):
        return iter(self.students)
c1 = Classroom(["Tom", "Jerry", "Alice"])
for student in c1:
    print(student)


# 对象加法：__add__
# 1. 字符串和数字类型相加本质上也是魔法方法
numbers = numbers + [4, 5, 6]
message = "Hello, " + "world!"

# 2. 对自定义类型实现 __add__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)


# 对象布尔值：__bool__
# 1. Python 如何判断对象真假:
# 我们自己定义的对象默认一般为 True
print(bool(s1)) # True

# 2. 对自定义类型实现 __bool__
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)

    # 当购物车为空时， 返回 False
    def __bool__(self):
        return len(self.items) > 0

cart = ShoppingCart()
print(bool(cart))
