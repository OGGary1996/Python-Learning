# Python 代码的常见运行方式
# 1. 直接运行文件: python path/to/app.py
# 此时：
# - app.py 的 __name__ 是 "__main__"
# - 文件被当作入口脚本，而不是按完整模块名导入
# - sys.path[0] 通常与入口脚本所在目录有关
# - 包内相对导入可能失去包上下文

# 2. 在项目根目录使用 -m 运行模块: python -m myapp.app
# 此时：
# - Python 先通过导入系统定位 myapp.app
# - 被执行模块的 __name__ 是 "__main__"
# - __package__ 保留正确的包上下文
# - 包内绝对导入和相对导入能够按模块结构工作


# __main__.py
# 如果包中存在 __main__.py，可以直接使用 python -m 包名 运行该包： python -m myapp
# myapp/
# ├── __init__.py
# ├── __main__.py
# └── app.py
# Python 会执行 myapp/__main__.py

