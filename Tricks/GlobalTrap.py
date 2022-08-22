#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : GlobalTrap.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-08-22 23:27:19
# Last Modified Date: 2022-08-22 23:27:19
# Last Modified By  : sandwich <122079260@qq.com>
"""
演示全局变量带来的陷阱
"""

functions = []

for n in range(8):

    def f():
        return f.index

    f.index = n
    functions.append(f)

# 列表表达式优先全局变量
print([f() for f in functions])

lst = []
# for loop 优先局部变量
for f in functions:
    lst.append(f())

print(lst)
