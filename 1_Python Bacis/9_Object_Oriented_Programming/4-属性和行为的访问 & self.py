# 属性和行为
# 1. 属性表示对象有什么
# Student 对象
# ├── name = "Tom"
# ├── age = 20
# └── score = 95
# name, age, score 都是对象的属性

# 2. 行为表示表示对象能做什么
# 在 Python 中，对象的行为就是类中的方法。

# 3. 方法 method 和 函数 function
# 函数：独立存在，一等公民，可以作为参数传递；直接单独调用
# 方法：存在于类内部，通过对象进行调用


# 类外部调用方法
# 1. 最常见的方式 对象.方法()
class Student:
    def introduce(self):
        print("Hello, I am a student.")
stu = Student()
stu.introduce()

# 2.通过类名.方法()+对象作为参数传递调用
Student.introduce(stu)

# 3. 底层理解
# 当我们写 对象.方法() 时，Python内部会解释为类名.方法()+对象作为参数传递调用
# 对象.方法() 本质上是：类.方法(对象)
# 所以类中的方法的第一个参数必须显式声明为self


# 类内部调用方法
# 1. 使用 self.method() 调用内部方法
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def info(self):
        print(f"Student's name is {self.name}, age is {self.age}, score is {self.score}.")

    def greet(self):
        print("Hello, I am a student.")
        # 这里 self.method() 表示调用内部的方法
        self.info()
stu = Student("Tom", 29, 100)
stu.greet()
# 2. 为什么必须要加上 self
# 如果不加 self 表示为使用全局方法，但是全局方法此时没有定义

# 3. 底层理解
# 还是一样的道理：当我们写 对象.方法() 时，Python内部会解释为类名.方法(对象)
# 当调用的方法中包含了内部方法时，对象已经作为 self 传递进去了


# 类外部访问和修改属性
# 1. 访问：通过 对象.属性
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Tom", 20)
print(student.name)
print(student.age)

# 2. 修改：通过 对象.属性
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Tom")
student.name = "Jerry"
print(student.name)
# 注意：虽然 Python 可以这么做，但是不建议通过这种方式直接修改属性的值，这样会导致对象的结构统一被破坏
student.age = 20 # 此时新增了一个属性

# 3. Python 和 Java 的区别
# Java 通常不会直接访问属性，而是通过 getter / setter
# Python 社区的主流理念恰恰相反,不推荐一开始就手写 getter/setter,
# 这是因为 Python 有一个"杀手锏"特性—— @property 装饰器，可以让你在不改变调用方式的前提下，随时把一个普通属性"升级"成带逻辑的属性。
class Student:
    def __init__(self, name):
        self._name = name
    @property # 相当于 getter,将 _name 暴露为一个 name 方法
    def name(self):
        return self._name
    @name.setter # 相当于 setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Name cannot be empty")
        self._name = new_name

stu = Student("Tom")
print(stu.name) # 调用方式和普通的属性一样，没有方法的括号()
stu.name = "Jerry" # 赋值方式也和普通的属性一样，直接赋值，而不是调用方法
# 调用方看到的、写的代码，和直接访问属性完全一样（stu.name，不是 stu.get_name()）。
# setter/getter 逻辑对调用方完全透明。


# 类内访问和修改属性
# 1. 访问：通过 self 直接访问
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我叫 {self.name}，今年 {self.age} 岁")

student = Student("Tom", 20)
student.introduce()
# 注意：局部变量和对象属性的区别：

# 2. 设置：通过 __init__ ，这是最规范的做法

# 3. 新增：通过普通方法
class Student:
    def __init__(self, name):
        self.name = name

    def set_score(self, score):
        self.score = score

student = Student("Tom")
student.set_score(95)
print(student.name)
print(student.score)

# 4. 修改：通过普通方法
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, points):
        self.score += points


student = Student("Tom", 80)
student.add_score(10)
print(student.score)


# self 的底层理解
# 1. self 表示正在操作对象本身

# 2. 不同对象调用方法时，self 不同，由于不同对象的属性也不同

# 3. 方法第一个参数要写 self
# 当我们写 对象.方法() 时，Python内部会解释为类名.方法(对象)

# 4. 验证 self 指向对象
class Demo:
    def print_self(self):
        print(self)
demo = Demo()
# 直接打印对象地址
print(demo)
# 对象内部的方法打印对象的地址
demo.print_self()

# 5. Python 中的 self 并不是关键字，并且必须要显式声明；这和 Java 中的 this 关键字不同，并且 this 关键字可以隐式声明


# 完整案例：类内部/外部 访问和修改属性，类内部/外部访问方法
class Student:
    def __init__(self, name, age):
        # 类内设置对象属性
        self.name = name
        self.age = age
        self.score = 0

    def set_score(self, score):
        # 类内修改对象属性
        self.score = score

    def get_level(self):
        # 类内访问对象属性
        if self.score >= 90:
            return "优秀"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"

    def introduce(self):
        # 类内调用自己的另一个方法
        level = self.get_level()
        print(f"我叫 {self.name}，今年 {self.age} 岁，成绩等级是：{level}")


# 类外创建对象
student = Student("Tom", 20)

# 类外设置对象属性
student.score = 95

# 类外访问对象属性
print(student.name)
print(student.score)

# 类外调用对象方法
student.introduce()

# 类外通过方法修改属性
student.set_score(58)

# 再次调用方法
student.introduce()