#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : usefunc.py
# Author            : sandwich
# Date              : 2022-10-24 16:39:09
# Last Modified Date: 2022-10-30 21:26:22
# Last Modified By  : sandwich

from urllib.parse import parse_qs

if __name__ == "__main__":
    my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
    print(my_values)
    print("Red:", my_values.get("red"))
    print("Green:", my_values.get("green"))
    print("Opacity:", my_values.get("opacity"))

    red = my_values.get("red", [""])[0] or 0
    green = my_values.get("green", [""])[0] or 0
    opacity = my_values.get("opacity", [""])[0] or 0

    print("Red:      %r" % red)
    print("Green:    %r" % green)
    print("Opacity:  %r" % opacity)
