#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : string_module.py
# Author            : sandwich
# Date              : 2023-05-18 22:50:36
# Last Modified Date: 2023-05-30 09:49:31
# Last Modified By  : sandwich

import string

if __name__ == "__main__":
    s = 'sfdfggyg122300'
    num = 0

    for i in s:
        if i in string.ascii_letters:
            num += 1
    print(num)

    s = 'Split the argument into words using split, capitalize each'

    print(string.capwords(s))
