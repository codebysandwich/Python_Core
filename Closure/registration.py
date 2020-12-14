#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : registration.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2020-12-14 10:47:08
# Last Modified Date: 2020-12-14 10:47:08
# Last Modified By  : sanwich <122079260@qq.com>

registry = []

def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func


