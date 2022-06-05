# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2022-03-29 09:51:46
@LastEditTime: 2022-03-29 09:51:46
@LastEditors: sandwich
@Description: In User Settings Edit
@FilePath: /Python_Core/Closure/ClosureDemo.py
'''


def pow(power):

    def wrapper(num):
        return num ** power

    return wrapper


def myfilter(iterable):

    def wrapper(low, up):
        for item in iterable:
            if low < item < up:
                yield item

    return wrapper


if __name__ == "__main__":
    pow_3 = pow(3)
    print(pow_3(2))

    l = [9, 1, 3, 12, 0, -8, 13]
    f_ = myfilter(l)
    for i in f_(0, 6):
        print(i)
