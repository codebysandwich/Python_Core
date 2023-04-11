#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : tt.py
# Author            : sandwich
# Date              : 2023-02-24 15:42:20
# Last Modified Date: 2023-02-24 15:44:19
# Last Modified By  : sandwich


class Person:

    def __init__(self, name):
        self.name = name

    @property
    def age(self):
        return 30


def test():
    print("hello world")


if __name__ == "__main__":
    test()
