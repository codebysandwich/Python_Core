#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : recursion.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2021-09-05 17:34:35
# Last Modified Date: 2023-04-25 14:22:00
# Last Modified By  : sandwich


class Doll:

    def __init__(self, code, contain, item):
        self.code = code
        self.contain = contain
        self.item = item


def find_doll(doll, contain):
    if doll.contain == contain:
        return doll.code
    else:
        # 将结果递归
        return find_doll(doll.item, contain)


if __name__ == "__main__":
    d1 = Doll("1", "candy", None)
    d2 = Doll("2", "diamond", d1)
    d3 = Doll("3", "whistle", d2)
    d4 = Doll("4", "toy", d3)

    # d = d4
    # while d.item:
    #     print(d.contain)
    #     d = d.item

    code = find_doll(d4, "diamond")
    print(code)
