# 模块的导入

# import 做了什么：import 用于查找并加载模块，然后在当前作用域中绑定一个名称。
import math
print(f"100 Square root is {math.sqrt(100)}")
# 这里的 math 是当前文件中的模块名称，sqrt 是 math 模块命名空间中的函数。


# 常见导入方式
# 1. 导入整个模块
import math

# 2. 导入模块中某个函数
from math import sqrt

# 3. 同时导入模块中的多个函数
from math import sqrt, floor
from pathlib import (
	Path,
	PurePath,
	PurePosixPath,
)

# 4. 别名：当模块名称过长或者可能存在命名冲突时使用
import datetime as dt
from datetime import datetime as dt


# 两种导入方式的区别
# 1. 在当前作用域绑定模块
import math
# 2. 在当前作用域绑定函数
from math import sqrt
# 如果模块内部的名称后来被重新赋值，已经通过 from 导入的名称不会自动重新绑定
from math import sqrt as square_root
print(square_root(9))
print(sqrt(9))
# 因此，需要持续读取模块当前值的场景，更适合使用 import *** 后访问 ***.***。


# 命名冲突
# 不同模块可能提供同名函数，如果命名冲突，保留模块前缀
import module_a
import module_b
module_a.test()
module_b.test()
# 也可以使用别名
from module_a import test as a_test
from module_b import test as b_test
a_test()
b_test()


# 通配符导入，不推荐
from math import *
# 会把一大批来自 math 中的名称直接放入当前的作用域
# - 无法快速判断名称来自哪个模块
# - 容易覆盖当前作用域中的同名名称
# - IDE 和静态分析工具更难追踪名称来源
# - 模块新增公开名称后，调用方可能在不知情时受到影响


# 与 Java 导入的区别
# 两者表面语法相似，但行为不同：
# 1. Java 中的 import 主要用于简化类的全限定名，由编译器处理
# 2. Python 中的 import 会在运行时查找、创建并执行模块
# 3. Java 的 import package.* 不会递归导入子包
# 4. Python 的通配符导入会把名称绑定到当前作用域，因此更容易造成污染