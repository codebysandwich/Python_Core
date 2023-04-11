#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : NoValueType.py
# Author            : sandwich
# Date              : 2023-04-11 17:43:08
# Last Modified Date: 2023-04-11 17:55:30
# Last Modified By  : sandwich

if __name__ == "__main__":
    a = 1
    b = a
    print(a is b)
    print(id(a), id(b))
    b = 2
    print(id(a), id(b))
