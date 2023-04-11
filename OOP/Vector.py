# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2022-06-06 09:36:53
@LastEditTime: 2022-06-06 09:37:02
@LastEditors: sandwich
@Description: 重载运算符
@FilePath: /Python_Core/OOP/Vector.py
'''
from array import array
from itertools import zip_longest


class Vector:

    def __init__(self, *args) -> None:
        self._components = array('f', args)

    def __repr__(self) -> str:
        # return "Vector({})".format(', '.join(
        #     repr(item) for item in self._components))
        return "Vector{}".format(repr(tuple(self._components)))

    def __len__(self) -> int:
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __add__(self, other):
        try:
            pairs = zip_longest(self, other, fillvalue=0)
            return Vector(*(a + b for a, b in pairs))
        except TypeError:
            raise NotImplemented

    def __sub__(self, other):
        try:
            pairs = zip_longest(self, other, fillvalue=0)
            return Vector(*(a - b for a, b in pairs))
        except TypeError:
            raise NotImplemented

    def __mul__(self, other):
        ...


if __name__ == "__main__":
    v1 = Vector(2, 1, 4)
    v2 = Vector(1, 4)
    print(v1 - v2)
