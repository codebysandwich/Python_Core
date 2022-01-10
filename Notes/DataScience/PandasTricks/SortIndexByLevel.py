#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : SortIndexByLevel.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-01-10 15:31:27
# Last Modified Date: 2022-01-10 15:31:27
# Last Modified By  : sandwich <122079260@qq.com>

import numpy as np
import pandas as pd

if __name__ == "__main__":
    data = pd.DataFrame(
        {
            'angles': [0, 3, 4, 4, 5, 6],
            'degrees': [360, 180, 360, 360, 540, 720]
        },
        index=[['A', 'A', 'A', 'B', 'B', 'B'],
               [
                   'circle', 'triangle', 'rectangle', 'circle', 'triangle',
                   'rectangle'
               ]])
    print(data)
    print(data.sort_index(level=1))
