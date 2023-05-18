#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : func_dispatch.py
# Author            : sandwich
# Date              : 2023-04-13 21:01:52
# Last Modified Date: 2023-04-15 14:26:55
# Last Modified By  : sandwich

from functools import singledispatch


@singledispatch
def func(arg):
    print(f"default: value={arg}")


@func.register
def _(arg: int):
    print(f"number: value={arg}")


@func.register
def _(arg: float):
    print(f"number: value={arg}")


@func.register
def _(arg: str):
    print(f"string: value={arg}")


if __name__ == "__main__":
    func([1, 2])
    func(3.4)
    func(3)
    func("hello")
