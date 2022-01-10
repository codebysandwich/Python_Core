#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : args_collection.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-01-10 15:08:25
# Last Modified Date: 2022-01-10 15:25:38
# Last Modified By  : sandwich <122079260@qq.com>

import numpy as np


def get_mean(*args):
    """get_mean.

    Args:
        args: collections of arg
    """
    if args:
        arr = np.array(args)
        return round(np.mean(arr), 1)
    else:
        return np.nan


def show_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:  {v}")


if __name__ == "__main__":
    print(get_mean())
    print(get_mean(3, 4, 9))
    print(get_mean(3, 4, 9, 12))
    print(get_mean(3, 4, 9, 12, 99))

    print("======演示具名参数收集======")
    show_kwargs(a=1, b="test", dicts={"name": "sand", "age": 20})
