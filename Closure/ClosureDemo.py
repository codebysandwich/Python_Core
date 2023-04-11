#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ClosureDemo.py
# Author            : sandwich
# Date              : 2023-03-31 14:23:51
# Last Modified Date: 2023-03-31 14:52:46
# Last Modified By  : sandwich


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
