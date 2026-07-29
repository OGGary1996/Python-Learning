# __init__.py 的基本作用
# __init__.py 是普通包中的初始化模块。导入包时，Python 会执行该文件：
import shop
# 在同一个解释器进程中，包初始化通常只执行一次，之后从 sys.modules 复用包对象。


# 在 __init__.py 中初始化包
# 可以在 __init__.py 中定义包级常量或执行轻量初始化，可以直接访问
print(shop.VERSION)
print(shop.DEFAULT_CURRENCY)


# __all__ 属性
# __all__ 是一个字符串列表，用于声明通配符导入时应该导出的名称，当使用 * 通配符导入时，__all__ 决定了哪些内容会被导入
# 1. 没有__all__ 时：
# - 对于普通模块，通配符导入通常选择不以下划线开头的名称。
# - 对于包，`from package import *` 不会自动扫描文件系统并导入所有子模块。它只能使用包初始化后命名空间中已有的公开名称。
# 2. __all__ 不是权限控制，只在使用 * 通配符时生效，但仍然可以显式调用不在 __all__ 中的内容


# 包的公开名称和内部方法
# Python 通常使用单下划线表示内部实现：
# # shop/products.py
# def find_product(product_id):
# 	return _load_product(product_id)
# def _load_product(product_id):
# 	return {"id": product_id}
# _load_product() 仍然可以被访问，但下划线表达“它不是稳定公共接口”的约定。