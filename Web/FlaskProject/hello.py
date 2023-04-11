#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : hello.py
# Author            : sandwich
# Date              : 2022-12-01 17:50:17
# Last Modified Date: 2023-04-10 17:45:03
# Last Modified By  : sandwich

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"
