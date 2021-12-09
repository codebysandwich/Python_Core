#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : pool_example.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-03-25 17:57:23
# Last Modified Date: 2021-08-30 11:40:40
# Last Modified By  : sandwich <122079260@qq.com>

from multiprocessing import Pool, Manager, Lock, Semaphore
from random import random
from time import sleep

queue = []


def handle(factor, lock):
    # q.put(factor)
    with lock:
        queue.append(factor)
    print(queue)
    sleep(random())


if __name__ == "__main__":
    # queue = Manager().Queue()
    pool = Pool(10)
    lock = Manager().Lock()
    for i in range(20):
        pool.apply_async(handle, args=(i, lock))
    pool.close()
    pool.join()
    print("读取数据")
    # while not queue.empty():
    #     print(queue.get(True))
    print(queue)
