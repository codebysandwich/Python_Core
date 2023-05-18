#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : Vector.py
# Author            : sandwich
# Date              : 2023-04-25 15:05:04
# Last Modified Date: 2023-04-25 15:08:50
# Last Modified By  : sandwich

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
            raise NotImplementedError

    def __sub__(self, other):
        try:
            pairs = zip_longest(self, other, fillvalue=0)
            return Vector(*(a - b for a, b in pairs))
        # except TypeError:
        #     raise NotImplementedError
        except Exception as e:
            print(f"Exception: {e}")

    def __mul__(self, other):
        ...


if __name__ == "__main__":
    v1 = Vector(2, 1, 4)
    v2 = Vector(1, 4)
    print(v1 - v2)
    print(v1 - 4)
