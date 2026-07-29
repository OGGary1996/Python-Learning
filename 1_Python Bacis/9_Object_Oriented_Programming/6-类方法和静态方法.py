# Python 中常见的三种方法
# 1. 实例方法 Instance Method, 自动接收参数 self
# 2. 类方法 Class Method，自动接收参数 cls
# 3. 静态方法 Static Method， 什么都不自动接收


# 类方法 Class Method
# 1. 类方法是操作类本身的方法，需要使用装饰器 @classmethod
# 类方法的第一个参数通常写成 cls
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

s1 = Student("Tom")
s2 = Student("Jerry")
print(Student.get_count())

# 2. cls 表示当前类本身
# 在调用 Student.get_count(cls) 时候，cls 等于 Student 本身，所以会将 Student 作为参数 cls 传递给方法

# 3. 类方法的核心特征：
# 1. 使用 @classmethod 装饰器
# 2. 第一个参数通常写 cls
# 3. cls 表示当前类
# 4. 可以访问和修改类属性
# 5. 通常通过 类名.方法() 调用
# 6. 适合处理和类整体有关的逻辑

# 4. 类方法的底层调用过程
# 当我们写：Student.get_count() 时，等效于 Student.show_count(Student)，类方法自动接收cls作为方法参数传递

# 5. 类方法也可以通过对象调用，但是不推荐这种方式
print(s1.get_count())
# 本质上还是依赖于 Python 的调用链，但是不符合语意

# 6. 类方法可以用于修改类属性


# 类方法可以用于替代 __init__ 创建对象
# 1. 案例
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

s1 = Student.from_string("Tom,20")
print(s1.name)
print(s1.age)

# 2. 为什么用 cls，而不是直接写 Student， return Student(name, age)
# 因为这样更灵活，比如后面有子类继承 Student，用 cls 可以保证谁调用这个类方法，就创建谁的对象。


# 静态方法 Static Method
# 1. 静态方法是放在类内部的普通方法，不自动接受 self 和 cls 参数，需要使用装饰器 @staticmethod，
# 静态方法的使用不依赖对象的产生，这一点和Java类似，使用用于工具类中
class MathTool:
    @staticmethod
    def add(x, y):
        return x + y
# 2. 静态方法的核心特征
# 1. 使用 @staticmethod 装饰器
# 2. 不自动接收 self
# 3. 不自动接收 cls
# 4. 不能直接访问实例属性
# 5. 不能直接访问类属性
# 6. 本质上是放在类命名空间里的普通函数

# 3. 静态方法也可以使用对象调用，但是不推荐，不具备语意


# 完整案例
class Student:
    school = "ABC College"
    count = 0

    def __init__(self, name, age, score):
        self.name = name,
        self.age = age
        self.score = score
        # 修改类属性
        Student.count += 1

    # 实例方法：操作具体对象
    def introduce(self):
        print(f"我叫 {self.name}，今年 {self.age} 岁，成绩是 {self.score}")

    # 实例方法：根据对象自己的 score 判断是否及格
    def is_passed(self):
        return self.score >= 60

    # 类方法：操作类属性 count
    @classmethod
    def show_count(cls):
        print(cls.count)

    # 类方法：修改类属性 school
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # 类方法：通过字符串创建对象
    @classmethod
    def from_string(cls, data):
        name, age, score = data.split(",")
        return cls(name, int(age), int(score))

    # 静态方法：工具方法，判断分数是否合理
    @staticmethod
    def is_score_valid(score):
        return 0 <= score <= 100

s1 = Student("Tom", 20, 90)
s2 = Student.from_string("Jerry,25,85")

# 调用实例方法
s1.introduce()
s2.introduce()
print(s1.is_passed())
print(s2.is_passed())
# 调用类方法
Student.show_count()
Student.change_school("XYZ College")
# 调用静态方法
print(Student.is_score_valid(200))