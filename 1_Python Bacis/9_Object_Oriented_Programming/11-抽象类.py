# 为什么需要抽象类
# 1. 在学习多态时，我们写过类似代码：
class CreditCardPayment:
    def pay(self, amount):
        print(f"信用卡支付 {amount} 元")

class PaypalPayment:
    def pay(self, amount):
        print(f"PayPal 支付 {amount} 元")

def checkout(payment_method, amount):
    payment_method.pay(amount)

# 这段代码可以运行，因为 Python 支持鸭子类型
# 如果某个支付类忘记写 pay() 方法怎么办？

# 2. 抽象类解决的问题
# 提前规定子类必须实现哪些方法, 所以抽象类的核心价值是：定义规范，而不是直接完成所有功能。


# 什么是抽象类
# 1. 抽象类的核心概念:不能直接创建对象，主要用于被子类继承的类。
# 它通常会定义一些抽象方法: 父类只规定方法名字和参数,但不提供具体实现，要求子类必须自己实现。

# 2. 抽象类和普通类的区别: 抽象类不能直接创建对象, 给子类制定规则。


# Python 中如何定义抽象类
# 1. 使用 ABC 和 abstractmethod
from abc import abstractmethod, ABC

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# 2. 子类必须实现抽象方法
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"信用卡支付 {amount} 元")

payment = CreditCardPayment()
payment.pay(100)


# 抽象类的核心作用：统一接口
# 1. 抽象类定义统一行为
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"信用卡支付 {amount} 元")

class PaypalPayment(Payment):
    def pay(self, amount):
        print(f"PayPal 支付 {amount} 元")

class ApplePayPayment(Payment):
    def pay(self, amount):
        print(f"Apple Pay 支付 {amount} 元")

def checkout(payment: Payment, amount):
    payment.pay(amount)

checkout(CreditCardPayment(), 100)
checkout(PaypalPayment(), 200)
checkout(ApplePayPayment(), 300)

# 2. 抽象类让多态更规范
# 之前的鸭子类型是：只要你有 pay() 方法，我就能用你。
# 如果你继承了 Payment，你就必须有 pay() 方法。
# 所以抽象类比单纯鸭子类型更严格。


# 抽象类可以包含普通方法
# 1. 抽象类不一定全是抽象方法
class Payment(ABC):
    platform = "Online Payment"

    def __init__(self, user):
        self.user = user

    def log(self, amount):
        print(f"{self.user} 发起了一笔 {amount} 元的支付")

    @abstractmethod
    def pay(self, amount):
        pass
# 子类可以继承使用普通的方法
class CreditCardPayment(Payment):
    def pay(self, amount):
        self.log(amount)
        print(f"信用卡支付 {amount} 元")

payment = CreditCardPayment("Tom")
payment.pay(100)


# 抽象方法可以有方法体吗？
# 1. Python 抽象方法可以有默认实现
class Exporter(ABC):
    @abstractmethod
    def export(self, data):
        print("开始导出数据")

class PdfExporter(Exporter):
    def export(self, data):
        super().export(data)
        print(f"导出 PDF：{data}")

exporter = PdfExporter()
exporter.export("report data")

# 2. 为什么抽象方法还要写方法体
# 这种写法适合：父类提供公共前置逻辑，子类补充具体实现。


# 抽象类和接口思想
# 1. Python 没有完全等同于 Java interface 的语法，但可以通过 Mixin 来表达接口的思想

# 2. is-a vs can-do / has-a
# is-a（继承本质、共享状态和行为）可以使用 抽象类 来进行统一规定
# can-do（横向能力，可插拔） 可以使用 接口 / Mixin


# 抽象属性：@property + @abstractmethod
# 1.  抽象类不仅可以要求方法，也可以要求属性
# 有时候我们希望子类必须提供某个属性。
# 例如所有导出器都必须有一个 file_extension：
class Exporter(ABC):
    @property
    @abstractmethod
    def file_extension(self):
        pass

    @abstractmethod
    def export(self, data):
        pass

class PdfExporter(Exporter):
    @property
    def file_extension(self):
        return ".pdf"

    def export(self, data):
        print(f"导出 PDF 文件：{data}")

exporter = PdfExporter()
print(exporter.file_extension)
exporter.export("report data")


# 抽象类中的类方法和静态方法
# 1. 抽象类方法
# 抽象方法也可以和 @classmethod 结合。
# 例如要求每个子类都提供 from_config() 创建对象的方式：
class Model(ABC):
    @classmethod
    @abstractmethod
    def from_config(cls, config):
        pass

    @abstractmethod
    def predict(self, data):
        pass

class KNNModel(Model):
    def __init__(self, k):
        self.k = k

    @classmethod
    def from_config(cls, config):
        return cls(k=config["k"])

    def predict(self, data):
        print(f"使用 KNN 模型进行预测，k={self.k}，data={data}")

model = KNNModel.from_config({"k": 5})
model.predict([1.2, 3.4])

# 2.  抽象静态方法
# 抽象方法也可以和 @staticmethod 结合。
# 例如要求每个验证器都提供一个静态校验方法：
class Validator(ABC):
    @staticmethod
    @abstractmethod
    def validate(value):
        pass

class AgeValidator(Validator):
    @staticmethod
    def validate(value):
        return 0 <= value <= 150

print(AgeValidator.validate(20))
# print(AgeValidator.validate(-1))


# 抽象类和 Protocol 的区别
# 1. ABC 是显式继承

# 2. Protocol 更接近鸭子类型
# Protocol 来自 typing 模块。
# 它更强调 只要结构符合，就算满足协议。