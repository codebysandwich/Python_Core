#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : fString.py
# Author            : sandwich
# Date              : 2022-12-05 22:59:17
# Last Modified Date: 2023-04-13 20:54:04
# Last Modified By  : sandwich


def print_diamond(line, mark='*', space=' '):
    """print_diamond.
    控制台打印菱形
    Args:
        line: 菱形中轴线长度
        mark: 菱形符号
        space: 空白填充及填充符号
    """
    line = line + 1 if line % 2 == 0 else line
    mid = line - line // 2
    for i in range(line):
        if i < mid:
            print(f"{mark*(2*i+1):{space}^{line}s}")
        else:
            print(f"{mark*((line-i-1)*2+1):{space}^{line}s}")


if __name__ == "__main__":
    hour, minutes = 2, 33
    # 前导0写法
    print(f"{hour:02d}:{minutes:02d}")
    # 较为复杂的填充写法
    print(f"{hour:0>2d}:{minutes:2d}")
    print_diamond(21, mark=".")
