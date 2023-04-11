#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : InitList.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-04-29 15:40:34
# Last Modified Date: 2022-12-02 13:47:27
# Last Modified By  : sanwich <122079260@qq.com>


def append(item, lst=[]):
    '''
    初始化的lst会一直占用
    '''
    lst.append(item)
    return lst


if __name__ == "__main__":
    print(append(1))
    print(append(2))
    l = [3]
    print(append(99, l))
