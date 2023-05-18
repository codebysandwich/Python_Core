#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : example.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-03-25 15:48:40
# Last Modified Date: 2023-04-15 14:28:43
# Last Modified By  : sandwich

from multiprocessing import Pool, Queue, Process
from time import sleep
from random import random


def handle(q, factor):
    q.put(factor)
    print(factor)
    sleep(random())


if __name__ == "__main__":
    queue = Queue()
    pool = []
    for i in range(20):
        p = Process(target=handle, args=(queue, i))
        p.start()
        pool.append(p)
    for p in pool:
        p.join()
    print('读取队列')
    while not queue.empty():
        print(queue.get(True))
