# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2022-03-30 17:15:52
@LastEditTime: 2022-03-30 17:15:59
@LastEditors: sandwich
@Description: 使用类作为装饰器
@FilePath: /Python_Core/Closure/DecoByClass.py
'''

from time import time, sleep


class Timer:

    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwds):
        start = time()
        self.func(*args, **kwds)
        print("Time consuming: {}".format(time() - start))


@Timer
def func_test(a, b, c=3):
    sleep(0.3)
    print((a + b) * c)


if __name__ == "__main__":
    # func_test = Timer(func_test)
    func_test(3, 5)
    print(func_test)
