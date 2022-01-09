#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : loc_Noninclued.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-01-09 22:17:51
# Last Modified Date: 2022-01-09 22:17:51
# Last Modified By  : sandwich <122079260@qq.com>

import numpy as np
import pandas as pd

if __name__ == "__main__":
    data = pd.DataFrame(np.random.randint(0, 10, (4, 4)),
                        index=list('abcd'),
                        columns=list('ABCD'))

    idx_vars = list('abdf')
    # 不存在的索引用np.nan填充
    print(data.reindex(idx_vars))

    # 不存在进行过滤
    print(data.loc[data.index.intersection(idx_vars), :])
