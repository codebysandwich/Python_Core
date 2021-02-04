#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : git_addrs.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-01-25 11:38:17
# Last Modified Date: 2021-01-25 11:38:17
# Last Modified By  : sanwich <122079260@qq.com>
import re
import requests

URL_FMT = r'https://github.com.ipaddress.com/{}'


def get_host_info(partten):
    url = URL_FMT.format(partten)
    html = requests.get(url).text
    reg = re.compile(
        r'IP Address</th><td><ul class="comma-separated"><li>(.*?)</li>')
    host = reg.findall(html)[0].strip("'")
    if partten:
        return '{}\t{}'.format(host, partten)
    else:
        return '{}\t{}'.format(host, 'github.com')


if __name__ == "__main__":
    # url = url_fmt.format('')
    # print(reg.findall(html))
    # url = url_fmt.format('gist.github.com')
    # html = requests.get(url).text
    # print(reg.findall(html))
    urls = [
        '', 'gist.github.com', 'api.github.com', 'assets-cdn.github.com',
        'raw.githubusercontent.com'
    ]
    for url in urls:
        print(get_host_info(url))
