#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : property.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2021-12-06 20:51:10
# Last Modified Date: 2021-12-16 11:17:05
# Last Modified By  : sandwich <122079260@qq.com>


class Student:
    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError

    @name.deleter
    def name(self):
        self._name = ""


if __name__ == "__main__":
    # 实现name getter
    s = Student("sand")
    print(s)
    # 实现name setter
    print(s.name)
    s.name = "leo"
    print(s.name)
    del s.name
    print(s.name)
    # 触发setter的异常
    s.name = 123
