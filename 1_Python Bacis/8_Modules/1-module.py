# 分模块的重要性：模块化就是按照职责拆分代码，让每个文件或包负责一组相关功能。


# 模块的定义：模块（Module）是 Python 组织和复用代码的基本单元。最常见的模块是一个 `.py` 文件，其中可以包含变量、函数、类和可执行语句。
# 比如：
# project/
# ├── calculator.py
# └── main.py
# calculator.py 是一个源代码模块，它的模块名通常是 calculator。

# 注意：模块不知包括 .py 的文件：
# .py 文件是最常见的模块形式，但 Python 还可以导入：
# - 使用 Python 编写的源代码模块
# - 由解释器提供的内置模块，例如 `sys`
# - 使用 C 等语言编写的扩展模块
# - 包及包中的子模块


# 模块的命名空间
# 每个模块都有自己的命名空间，用来保存该模块中定义的名称。
# 导入模块后，可以通过 模块名.名称 访问其中的内容：
import prices
final_price = prices.price_cal(100)
print(f"Final price after tax: {final_price}")


# 模块的常见来源：
# 1. 标准库模块，随Python一起安装
# 数学运算，常见函数：sqrt(), ceil(), floor(), pow()
import math
print(f"100 Square root is {math.sqrt(100)}")
# 随机数生成，常见函数：random()随机生成数字可以提供随机数种子复现, randint()随机生成指定范围内的整数, randange()随机生成范围整数支持步长
import random
print(f"Random number is {random.random()}")
print(f"Random number between 1 and 100 is {random.randint(1, 100)}")
print(f"Random odd number between 1 and 100(excluded) is {random.randrange(1, 100, 2)}")
# 处理文件路径
import pathlib
print(pathlib.Path.cwd()) # 打印当前工作目录
print(pathlib.Path.home()) # 打印用户主目录
# 时间处理，常见函数：datetime.datetime.now()打印当前时间，datetime.timedelta()计算两个时间间隔
import datetime
print(f"Current time is {datetime.datetime.now()}")
print(f"Time difference is {datetime.datetime.now() - datetime.datetime.now()}")
# JSON 处理，常见函数：json.dumps()将对象转换为 JSON 字符串
import json
print(json.dumps({"name": "John", "age": 30}))
# 解释器和运行环境 sys，常见函数：sys.argv 打印命令行参数
import sys
print(sys.argv)

# 2. 自定义模块
import prices
final_price = prices.price_cal(100)
print(f"Final price after tax: {final_price}")

# 3. 第三方模块，第三方代码由 Python 社区或其他组织开发，通常需要先安装对应的发行包：
# 使用 pip：pip install requests
# 使用 conda: conda install requests
# 使用 uv: uv add requests，或者临时安装 uv pip install requests
# 注意：需要注意，pip 安装的是发行包（Distribution Package），import 导入的是模块或导入包。两者名称经常相同，但并不保证相同。


# 模块对象
# 模块被导入后，会在内存中表现为一个模块对象：
print(f"Type of math module is {type(math)}")
# 常见的模块属性：
# __name__ 该模块的名称
# __file__ 该模块的源文件路径
# __doc__ 该模块的文档字符串
# __package__ 该模块的包名称,如果为空字符串，则表示该模块是顶级模块，不在 package 下
# __spec__ 描述模块如何被找到和加载的信息
print(f"Name of math module is {math.__name__}")
print(f"File path of math module is {math.__file__}")
print(f"Documentation string of math module is {math.__doc__}")
print(f"Package name of math module is {math.__package__}")
print(f"Specification of math module is {math.__spec__}")