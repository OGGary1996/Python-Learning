# 执行 import example 时，可以把导入过程概括为：
# 1. 检查 sys.modules 中是否已经缓存模块
# 2. 如果没有缓存，使用导入查找器寻找模块规格（ModuleSpec）
# 3. 根据规格创建模块对象
# 4. 将模块对象放入 `sys.modules`
# 5. 执行模块代码，初始化模块命名空间
# 6. 在当前作用域绑定导入语句指定的名称
# 先放入缓存再执行代码，有助于处理递归导入，但也意味着循环导入时可能访问到“尚未初始化完成”的模块。


# sys.modules 模块缓存
# sys.modules 是一个字典，保存当前进程已经加载的模块：
import math
import sys
print( "math" in sys.modules)
print(sys.modules["math"] is math)


# sys.path 模块查找路径
# 对于需要从文件系统查找的模块，Python 会根据 sys.path 中的目录进行搜索：
# sys.path 通常由以下来源共同组成：
# - 入口脚本所在目录，或者当前工作目录，具体取决于启动方式
# - `PYTHONPATH` 环境变量配置的目录
# - Python 标准库目录
# - 环境中的 `site-packages` 目录
# - 启动配置添加的其他目录
for path in sys.path:
    print(path)


# 和 Java 加载的区别
# - Python 根据导入系统、sys.path 和 sys.modules 查找并缓存模块
# - Java 根据模块路径或类路径，由类加载器查找和加载类
# - Python 导入会执行模块顶层代码
# - Java 类初始化可能执行静态初始化逻辑，但普通 `import` 声明本身不是运行时加载操作


# 模块的关键属性：
import json
print(json.__name__) # 名称
print(json.__file__) # 所在文件位置
print(json.__package__) # 包上下文
print(json.__spec__) # 查找与加载模块所需要的信息


# 字节码缓存 __pycache__
# Python 执行源代码模块时，通常会先把源代码编译成字节码。符合缓存条件时，字节码会保存在 __pycache__ 目录中的 .pyc 文件
# 需要注意：
# - .pyc 是 Python 字节码缓存，不是 Java .class 文件的完全对应物
# - 缓存不会改变模块的导入语义，首次加载时仍要执行模块代码
# - __pycache__ 由解释器自动管理，通常不需要手动修改