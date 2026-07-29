# 什么是多继承
# 1. 多继承指的是一个子类继承多个父类， python 支持多继承，而 Java 不支持多继承
class Flyable():
    def fly(self):
        print("I can fly")

class Swimmable():
    def swim(self):
        print("I can swim")

class Duck(Flyable, Swimmable):
    pass
duck = Duck()
duck.fly()
duck.swim()
# Duck 同时继承了 Flyable 和 Swimmable

# 2. 多继承适合表达 能力组合
# - 多继承很适合表达多个能力的组合，这有点类似于 Java 中的接口的实现。
# - 接口的思想同样体现了能力，可以同时实现多个接口，而不是 is-a 的概念

# 3. Java 中不支持多继承，只能多接口实现
# - 多继承的概念类似于 Java 中的多接口实现
# - 并且接口于多继承都用于描述一个能力，而不是 is-a 的概念


# 多继承中的方法名称冲突
# 1. 如果多个父类有同名方法怎么办
class A:
    def hello(self):
        print("hello from A")
class B:
    def hello(self):
        print("hello from B")
class C(A, B):
    pass
c = C()
c.hello() # hello from A
# 这里我们写的是 C(A, B) 我们先写了A，所以整个调用顺序是 C -> A -> B

# 2. 查看 MRO(Method Resolution Order) 表示方法的解析顺序
print(C.mro())
# 结果： [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# 说明查找顺序是 C -> A -> B -> object


# 菱形继承
# 1. 什么是棱形继承
#         A
#       /   \
#      B     C
#       \   /
#         D
# 此时 B 和 C 都继承 A， D 多继承 B 和 C

# 2. 棱形继承的方法重名问题
class A:
    def hello(self):
        print("hello from A")
class B(A):
    def hello(self):
        print("hello from B")
class C(A):
    def hello(self):
        print("hello from C")
class D(B, C):
    pass
d = D()
print(D.mro()) # D -> B -> C -> A -> object
d.hello()
# 此时，MRO 的调用链找到B中的方法


# 使用 super() 配合多重继承
# 1. super 的含义发生了变化
# 在多重继承中，super 的意思不再是直接简单的找父类，而是根据 MRO 找到调用链中的下一个类
class A:
    def process(self):
        print("A's process")

class B(A):
    def process(self):
        print("B's process")
        super().process()

class C(A):
    def process(self):
        print("C's process")
        super().process()

class D(B, C):
    def process(self):
        print("D's process")
        super().process()

print(D.mro()) # D -> B -> C -> A -> object
d = D()
d.process() # D's process -> B's process -> C's process -> A's process
# 调用链条分析：
# - `d.process()` → 沿着 MRO `[D, B, C, A, object]` 查找，找到 `D.process`，打印 `"D process"`
# - `D.process` 里 `super().process()` → 在 MRO 中找 D 的下一个，是 `B`，打印 `"B process"`
# - `B.process` 里 `super().process()` → 注意：这里的 `super()` 不是"B 的父类 A"，而是**沿着 d 实例的完整 MRO 继续往后找**，B 的下一个是 `C`，打印 `"C process"`
# - `C.process` 里 `super().process()` → 继续往后，是 `A`，打印 `"A process"`
# - `A.process` 里 `super().process()` → MRO 中 A 后面是 `object`，`object` 没有 `process` 方法，链条结束

# 注意：这里 B 里的 super().process() 确实会调用 C.process，而不再是 B 的父类，
# 即使 B 和 C 在类定义上毫无关系（B 不是继承自 C，C 也不是继承自 B）。

# 这正是 super() 的精髓：它不是按"当前类的父类"查找，而是按实例的 MRO 顺序依次查找下一个类
# 整个继承体系里，A.process 只会被调用一次，因为 super() 看的是"实例的 MRO 上，我这个类后面是谁"，而不是"我自己写死的父类是谁"。这也是它能优雅解决菱形继承问题的根本原因。


# Python 多继承的使用建议
# 1. 多继承很灵活，但是尽量避免使用过于复杂的结构

# 2. 更推荐使用多继承表达不同的能力，而不是复杂的业务体，这和 Java 中的接口思想接近
class JsonSerializable:
    def to_json(self):
        print("Converting to JSON")
class Loggable:
    def log(self):
        print("Logging")
class User(JsonSerializable, Loggable):
    pass
# 这里 `JsonSerializable` 和 `Loggable` 更像能力, 这种多继承比较清晰。

# 3. 多继承中的父类最好设计成 Mixin
# Python 中常见的设计：Mixin 混入类，用于表示一种能力，而不是复杂的业务体对象
# 各个 Mixin 互不相干，但是又通过 MRO 相互串联起来
class JsonMixin:
    def to_json(self):
        return self.__dict__
class LogMixin:
    def log(self):
        print(f"Logging {self}")
class Student(JsonMixin, LogMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student("Tom", 20)
print(stu.to_json())
stu.log()

# 4. 关于 Python 多继承的一个额外提醒
# 一个类的继承链上，最多只应该有一个"is-a"的抽象基类（或普通基类），其余的父类都应该是"can-do"的 Mixin


# object：所有类的顶层父类
# 1. Python 中所有类最终都继承 object，即使没有显式声明继承关系

# 2. object 提供了一些基础能力，比如: __str__ __repr__ __eq__ __hash__


# 组合 (has-a) 优于继承 (is-a)
# 如果只是想复用功能，不一定要继承, 很多时候，把一个**对象作为属性组合**进来更清晰。
class Engine:
    def start(self):
        print("Engine is starting")
class Car:
    def __inti__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()