# Coroutine 协程
协程是运行在单线程中的“并发”，是程序层面额设计。通过IO阻塞时进行运行函数之间的切换(非调用)实现，避免多线程的线程调度获得更大的运行效率。

协程可以处理IO密集型程序效率问题，CPU密集型不是协程的长处，如果要充分发挥CPU的作用需要采用协程与多进程结合的方式。

## aysncio+aysnc/await
Py3.5+以后，为了简化和更好地支持异步IO，引入了`async`和`await`关键字，让coroutine程序更加简洁易读。

```python

```

<++>