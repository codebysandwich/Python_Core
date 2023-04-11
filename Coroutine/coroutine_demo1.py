#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : coroutine_demo1.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2020-12-10 10:38:03
# Last Modified Date: 2023-03-31 14:23:30
# Last Modified By  : sandwich

import asyncio


async def test(i):
    print("action, 进入IO等待……")
    # 等待异步回调完成
    await asyncio.sleep(i)
    print("异步完成")


if __name__ == "__main__":
    #
    loop = asyncio.get_event_loop()
    tasks = [test(i) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
