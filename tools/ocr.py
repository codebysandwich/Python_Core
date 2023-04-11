#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ocr.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-08-22 14:22:06
# Last Modified Date: 2022-08-22 14:22:06
# Last Modified By  : sandwich <122079260@qq.com>

from cnocr import CnOcr

if __name__ == "__main__":
    ocr = CnOcr()
    file = r'/Users/caizhiming/Downloads/test.png'
    res = ocr.ocr(file)
    for val in res:
        print(val['text'])
