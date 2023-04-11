#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : GlobalTrap.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-08-22 23:27:19
# Last Modified Date: 2022-10-24 23:12:30
# Last Modified By  : sandwich
"""
演示全局变量带来的陷阱
"""

functions = []

for n in range(8):

    def f():
        return f.index

    f.index = n
    functions.append(f)
if __name__ == "__main__":
    # 列表表达式优先全局变量
    # 全局指向的f(), 等价 [f() for i in functions]
    print([f() for f in functions])

    lst = []
    # for loop 优先局部变量
    for f in functions:
        lst.append(f())

    print(lst)
