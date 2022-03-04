#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : deco.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2020-12-14 10:24:08
# Last Modified Date: 2022-02-27 12:16:21
# Last Modified By  : sandwich <122079260@qq.com>


def deco(func):

    def inner():
        print("running inner()")

    return inner


# @deco
# def target():
# print("running target()")


def target():
    print('running target()')


if __name__ == "__main__":
    target = deco(target)
    target()
