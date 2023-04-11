#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : AutoOverride.py
# Author            : sandwich
# Date              : 2022-10-19 16:49:28
# Last Modified Date: 2023-03-31 14:54:37
# Last Modified By  : sandwich


class A:
    __valid_kwds = ["a"]

    def __init__(self, **kwargs) -> None:
        # print(self.valid_kwds)
        for key, val in kwargs.items():
            if key in self.__valid_kwds:
                print(key, val)


class B(A):
    __valid_kwds = ["b"]

    def __init__(self, **kwargs) -> None:
        left_kwargs = {}
        for key, val in kwargs.items():
            if key in self.__valid_kwds:
                print(key, val)
            else:
                left_kwargs[key] = val
        super().__init__(**left_kwargs)


if __name__ == "__main__":
    o = B(a=2, b=3)
    print(o.__dir__())
