#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : self_used.py
# Author            : sandwich <122079260@qq.com>
# Date              : 2022-09-07 00:44:35
# Last Modified Date: 2022-09-07 00:44:35
# Last Modified By  : sandwich <122079260@qq.com>


class Air:

    def pick(self):
        print("pick")

    @staticmethod
    def tt():
        print('test')

    def pit(self):
        self.pick()
        Air.tt()


if __name__ == "__main__":
    a = Air()
    a.pit()
