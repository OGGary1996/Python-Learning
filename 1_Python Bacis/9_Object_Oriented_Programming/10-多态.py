# 什么是多态
# 1. 多态的核心概念： 同一个方法调用，作用在不同对象上，可以产生不同的行为。


# 多态解决什么问题
# 1.没有多态时的问题
class Dog:
    def speak(self):
        print("汪汪汪")

class Cat:
    def speak(self):
        print("喵喵喵")

def make_sound(animal):
    if isinstance(animal, Dog):
        animal.speak()
    elif isinstance(animal, Cat):
        animal.speak()

dog = Dog()
cat = Cat()
make_sound(dog)
make_sound(cat)

# 2. 有多态概念之后
def make_sound(animal):
    animal.speak()
make_sound(dog)
make_sound(cat)


# Python 多态的核心：鸭子类型 Duck Typing
# 1. 什么是鸭子类型: 如果一个东西走起来像鸭子，叫起来像鸭子，那它就可以被当作鸭子。
# 我不关心你是什么类型。我只关心你有没有我需要的方法。
class Dog:
    def speak(self):
        print("汪汪汪")

class Robot:
    def speak(self):
        print("我是机器人，正在发声")

class Person:
    def speak(self):
        print("你好")

def make_sound(obj):
    obj.speak()

make_sound(Dog())
make_sound(Robot())
make_sound(Person())


# 多态和类型注解
# 1. Python 可以给多态加类型提示
# Python 是动态语言，不强制类型声明; 但是为了代码更清楚，可以使用类型注解：帮助 IDE、类型检查工具和开发者理解代码。

# 2. 使用 Protocol 表达结构化类型
# Python 还有一种更接近鸭子类型的类型注解方式：
from typing import Protocol

class Payable(Protocol):
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment:
    def pay(self, amount: float) -> None:
        print(f"信用卡支付 {amount}")

class PaypalPayment:
    def pay(self, amount: float) -> None:
        print(f"PayPal 支付 {amount}")

def checkout(payment: Payable, amount: float) -> None:
    payment.pay(amount)

checkout(CreditCardPayment(), 100)
checkout(PaypalPayment(), 200)


