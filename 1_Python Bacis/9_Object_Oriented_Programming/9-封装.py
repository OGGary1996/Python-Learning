# 什么是封装
# 1. 封装的核心概念
# 把对象的数据和操作数据的方法放在一起，并控制外部如何访问这些数据。
# 也就是说，一个对象不应该只是“暴露一堆数据”，而应该把自己的数据和行为组织起来。

# 2. 没有封装的问题
# 如果没有封装，那么外部可以修改对象内部状态，这显然不合理
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

account = BankAccount("Tom", 1000)
account.balance = 2000


# 封装的本质：隐藏细节，暴露接口
# 1. 隐藏细节: 对象内部怎么保存数据、怎么计算、怎么维护状态，外部不需要知道。

# 2. 暴露接口: 对象对外提供一组安全、清晰的方法，让外部通过这些方法使用对象。
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdrawal(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self._balance < amount:
            raise ValueError("Insufficient balance")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

account = BankAccount("Tom", 1000)
account.deposit(500)
account.withdrawal(200)
print(account.balance)


# Python 中的访问控制
# 1. Python 没有 Java 那种严格 private，只是命名约定，而不是严格的权限控制

# 2. 公开属性 name, 单下划线属性 _name, 双下划线属性（防止子类覆盖） __name

# 3. 双下划线会触发 Python 的属性名称修改，比如：
class User:
    def __init__(self, password):
        self.__password = password
user = User("123456")
# print(user.__password) # Python 此时会把这个属性的名称修改掉，无法通过原名称访问


# 封装不是“全部私有化”
# 1. Java 风格的封装，通常通过 Getter/Setter

# 2. Python 不推荐无脑 Getter/Setter

# 3. Python 更推荐： 普通属性直接公开，需要控制内部细节使用单下划线配合@property, 涉及具体业务逻辑时，设计具体的业务方法


# 使用方法进行封装
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于 0")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("取款金额必须大于 0")
        if amount > self._balance:
            raise ValueError("余额不足")
        self._balance -= amount

    def get_balance(self):
        return self._balance

account = BankAccount("Tom", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())


# 使用 `@property` 进行封装
# 1. 什么是 @property：可以把一个方法伪装成属性访问，
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

student = Student("Tom")
print(student.name) # 注意，不是name() 也不是 _name

# 2. 只读属性
# 如果只写 getter，不写 setter，这个属性就是只读的。
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

account = BankAccount("Tom", 1000)
print(account.balance)

# 3. 可读可写属性
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能小于 0")
        self._age = value

student = Student("Tom", 20)
print(student.age)
student.age = 21
print(student.age)
# student.age = -10 报错，会触发setter的验证逻辑


# 封装中的业务方法
# 1. 什么时候不用 setter，而用业务方法
# 有些属性不应该被简单赋值，而应该通过业务动作修改。

# 2. 订单状态也适合通过业务方法修改，不推荐直接使用 setter
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self._status = "created"

    @property
    def status(self):
        return self._status

    def pay(self):
        if self._status != "created":
            raise ValueError("只有已创建的订单才能付款")
        self._status = "paid"

    def cancel(self):
        if self._status == "shipped":
            raise ValueError("已发货订单不能取消")
        self._status = "cancelled"

    def ship(self):
        if self._status != "paid":
            raise ValueError("只有已付款订单才能发货")
        self._status = "shipped"

order = Order("O001")
order.pay()
order.ship()
print(order.status)


# 封装和继承的关系
# 1. 子类可以访问父类的公开成员
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def introduce(self):
        print(f"我叫 {self.name}")

student = Student("Tom")
student.introduce()

# 2. 单下划线属性：子类可以访问，但要谨慎
class Person:
    def __init__(self, name):
        self._name = name

class Student(Person):
    def introduce(self):
        print(f"我叫 {self._name}")

# 3. 双下划线属性：避免子类误覆盖
class Parent:
    def __init__(self):
        self.__value = "parent"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "child"

child = Child()
print(child.__dict__)
# Parent 的 __value 被改写成 _Parent__value
# Child 的 __value 被改写成 _Child__value