#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : splitAndstarInFunc.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-01-27 14:23:02
# Last Modified Date: 2023-04-09 13:28:35
# Last Modified By  : sandwich

def func(a, b, /, f, g, *, e):
    """func.
        / 之前必须使用位置区分，* 之后必须使用参数名来限定，
        两者之间的位置与参数名均可区分
    """
    print(a, b, e, f, g)

    print("OK")


if __name__ == "__main__":
    func(1, 2, 5, g=19, e=6)
