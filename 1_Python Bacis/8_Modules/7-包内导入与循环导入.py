# 绝对导入：绝对导入从顶层包名称开始写出完整路径：
# 相对导入：相对导入以当前模块所属的包为起点：
# - . 表示当前包
# - .. 表示上一级包
# - ... 表示再上一级包


# 注意：为什么直接运行子模块可能失败
# 比如：
# myapp/
# ├── __init__.py
# ├── config.py
# └── services/
#     ├── __init__.py
#     ├── email.py
#     └── report.py
# 假设 report.py 使用相对导入：from .email import send_email
# 此时文件被当作顶层脚本执行，缺少 myapp.services 包上下文，相对导入可能出现：ImportError: attempted relative import with no known parent package


# 什么是循环导入
# 当模块 A 导入模块 B，而模块 B 在初始化完成前又导入模块 A，就形成循环导入。
# Python 开始加载 `module_a` 后，会先把模块对象放入 `sys.modules`，再执行代码。
# 执行到导入 `module_b` 时，`module_b` 又尝试从尚未完成初始化的 `module_a` 获取 `function_a`，
# 因此可能出现“partially initialized module”相关错误。