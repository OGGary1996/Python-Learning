from typing_extensions import override

# 1. 封装：把属性和方法放在一个类中，并且控制外部如何访问内部数据。
# 封装的意义：代码更清晰，职责和逻辑更明；外部不需要知道内部实现细节，保护内部对象状态
# Python 中约定使用 下划线_ 来表示内部属性；Java 中使用 private protect
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
    def get_owner(self):
        return self.owner
    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount must be positive")
            return
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Withdraw amount must be positive")
            return
        if self._balance < amount:
            print("Insufficient balance")
            return
        self._balance -= amount
# 这里的 _balance 表示内部属性，但是只是命名约定，并不像是 Java 中的强制性规定


# 2. 继承
# 与Java一样，可以继承父类已有的属性和方法，并且可以重载方法和改写属性
# 但是注意：子类可以访问父类的属性和方法，但是父类不能访问子类的属性和方法
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
animal = Animal()
animal.eat()
# animal.bark() 报错
dog = Dog()
dog.eat()
dog.bark()
# 这里 Dog 继承了父类的eat方法，并且扩写了bark方法

# 方法重写
class Cat(Animal):
    @override(Animal)
    def eat(self):
        print("Cat is eating")
    def meow(self):
        print("Cat is meowing")
# 与Java 中的 @Override 类似
# 这里的 Cat 类重写了eat方法，并且扩写了 meow 方法

# 使用 super() 调用父类的属性和方法
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major
stu = Student("Alice", "Computer Science")
#  类似于 Java 中的 super() 方法
# class Student extends Person {
#     private String studentId;
#
#     public Student(String name, String studentId) {
#         super(name);
#         this.studentId = studentId;
#     }
# }


# 3. 多态：同一个方法调用，在不同的对象中表现出不同的行为
# 						多态 (Polymorphism)
#                   "同一操作，不同行为" 这个现象/能力
#                        /                    \
#                       /                      \
# 			       基于继承实现              基于鸭子类型实现
# 			    （通过方法重写达成）        （不需要继承，只要接口/方法名一致）

# 基于继承实现
class Animal:
    def speak(self):
        raise NotImplementedError
class Cat(Animal):
    @override(Animal)
    def speak(self):
        print("Meow")
class Dog(Animal):
    @override(Animal)
    def speak(self):
        print("Woof")

def make_sound(animal):
    animal.speak()
# 这里 Dog 和 Cat 都重写了 Animal 的 speak 方法，然后 make_sound 函数统一调用 .speak()，展现出多态行为。
# 这种情况下，方法重写是实现多态的手段。

# 基于鸭子类型实现
# 在 Java 中，多态通常通过继承或者接口实现来实现，但是 Python 中可以通过鸭子类型实现（没有实现接口的语法）
class Duck:
    def speak(self):
        print("Quack")
class Robot:
    def speak(self):
        print("Robot is speaking")
def make_it_speak(obj):
    obj.speak()
# Duck 和 Robot 之间毫无继承关系，甚至没有共同的基类，但因为它们都有同名的 speak() 方法，make_it_speak 函数依然能对它们表现出统一的调用方式、不同的行为——这也是多态。
# 这就是"鸭子类型"式多态。