# 为什么需要包
# 模块可以拆分单个文件，但大型项目仍然可能包含大量模块。包（Package）用于把相关模块和子包组织到同一个命名空间下。
# shop/
# ├── __init__.py
# ├── products.py
# ├── orders.py
# └── payments/
#     ├── __init__.py
#     └── card.py
# - `shop` 是包
# - `shop.products` 和 `shop.orders` 是子模块
# - `shop.payments` 是子包
# - `shop.payments.card` 是子包中的模块


# 与模块的关系
# 1. 从导入系统的角度看，包是一种能够包含子模块的模块。导入包后得到的仍然是模块对象
import shop
print(type(shop))
print(shop.__name__)
# 2. 普通模块通常对应一个 `.py` 文件，包则具有用于搜索子模块的位置。包对象通常还拥有 __path__ 属性
import shop.payments as payments
print(payments.__path__)


# 普通包与命名空间包：
# 1. 普通包通常是包含 __init__.py 的目录，即使 __init__.py 是空文件
# 2. 从 Python 3.3 开始，某些没有 `__init__.py` 的目录也可以组成命名空间包（Namespace Package）。
# 命名空间包允许同一个包的不同部分分布在多个搜索路径中。
# location_a/
# └── company/
#     └── analytics/
#         └── report.py
# location_b/
# └── company/
#     └── billing/
#         └── invoice.py
# 如果 `location_a` 和 `location_b` 都在模块搜索路径中，`company` 可以成为跨目录的命名空间包。


# 导入包和子模块
# 1. 只导入包，但不会保证自动导入目录下的所有子模块，因为子模块可能在其他目录中
import shop
# 2. 导入子模块
import shop.products
# 3. 或者使用 from ... import ...
from shop import products


# 与 Java package 的简单对比
# - Python 普通包主要由目录、__init__.py 和导入系统共同形成
# - Java 通过 package 关键字声明类所属的命名空间，目录通常与包名保持一致
# - Python 包在导入时会创建并执行包模块
# - Java package 本身不是一个会执行初始化代码的对象
# - Python 支持跨多个路径组成的命名空间包