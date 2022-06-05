# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2022-03-31 09:01:26
@LastEditTime: 2022-03-31 09:14:46
@LastEditors: sandwich
@Description: 装饰类的装饰器介绍
@FilePath: /Python_Core/Closure/DecoClass.py
'''


def add_str(cls):

    def __str__(self):
        return str(self.__dict__)

    cls.__str__ = __str__
    return cls


@add_str
class Vector:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


if __name__ == "__main__":
    # Vector = add_str(Vector)
    v = Vector(3, 5)
    print(v)