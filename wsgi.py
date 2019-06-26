#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
from os.path import abspath
from os.path import dirname

# 设置当前目录为工作目录
# python程序中使用 import XXX 时，python解析器会在当前目录、已安装和第三方模块中搜索 xxx，如果都搜索不到就会报错
# 使用sys.path.append()方法可以临时添加搜索路径，方便更简洁的import其他包和模块。
# sys.path.insert(1, "")定义搜索路径的优先顺序，序号从0开始，表示最大优先级
# sys.path.insert()加入的也是临时搜索路径，程序退出后失效。
sys.path.insert(0, abspath(dirname(__file__)))

# 引入 app.py
import app

# 必须有一个叫做 application 的变量
# gunicorn 需要的就是这个变量
# 这个变量的值必须是 Flask 实例
# 这是规定的套路(协议)
application = app.app