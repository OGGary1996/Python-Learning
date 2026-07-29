# 继承
# 1。继承的核心：
# 让一个类复用另一个类已经定义好的属性和方法。


# 2. 继承的作用：
class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

dog = Dog()
dog.eat()
dog.sleep()
dog.bark()

cat = Cat()
cat.eat()
cat.sleep()
cat.meow()
# Dog 和 Cat 都继承了 Animal 类，所以它们都可以调用 Animal 类定义的属性和方法


# 继承的基本语法
# 1. Python 中使用 子类(父类) 的写法

# 2. Java 中使用 extend 关键字的写法


# 继承表示 is-a 的关系
# 1. 继承表示 是什么 的概念，比如 Dog is Animal, Cat is Animal

# 2. has-a 关系更多应该使用组合而不是继承
class Engine():
    def start(self):
        print("Engine is starting")
class Car():
    def __init__(self):
        self.engine  = Engine()
    def start(self):
        self.engine.start()

car = Car()
car.start()


# 单继承
# 1. 什么是单继承：一个子类只继承一个父类

# 2. 子类可以有自己的方法和属性

# 3. 子类可以重写父类的方法
class Animal:
    def speak(self):
        print("Animal is speaking")
class Dog(Animal):
    def speak(self):
        print("Dog is barking")
class Cat(Animal):
    def speak(self):
        print("Cat is meowing")


# 使用 super() 调用父类的方法
# 1. 为什么需要使用 super()：有时候子类需要扩展父类逻辑，而不是完全替换父类逻辑。
# 比如父类 Person 中已存在一个name属性，子类 Student 中想新增一个 student_id 属性
# 如果此时子类中直接重写 __init__ 方法，而不加上 super() 则父类的 __init__ 方法不会被调用，初始化失败

# 2. 正确写法：
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

stu = Student("Alice", 123)
print(stu.name)
print(stu.student_id)
# 这里的 super().__init__(name) 调用了父类的__init__() 方法

# 3. super() 的作用：
# - 直接调用父类的方法
# - 在方法中复用父类的逻辑
# - 在 多重继承 中配合 MRO 调用链查找下一个类

# 4. Java 中的 super()
# Java 中的构造函数与 Class 名称重合，所以调用父类的构造器直接使用 super()
# 调用父类其他方法使用 super.method()


# 继承中的属性查找顺序：
# 1. 在继承中，会先查找对象本身，然后查找类，然后查找父类
class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    pass

dog = Dog()
dog.speak() # dog 对象和 Dog 类都没有 speak()，会查找 Animal 父类

# 2. 查看继承关系
# isinstanceof()
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
# issubclass()
print(issubclass(Dog, Animal))