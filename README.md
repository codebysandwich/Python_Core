# Python_Core
+ 目的

展现原生python细节及高级Python使用方法
<!-- vim-markdown-toc GFM -->

* [Foundation](#foundation)
* [Iterator](#iterator)
* [Closure](#closure)
* [MultiThread](#multithread)
* [MultiProcessing](#multiprocessing)
* [Coroutine](#coroutine)

<!-- vim-markdown-toc -->


# Foundation
+ [Tutorial][tutorial]简单介绍了python的数据结构和基本流程控制以及函数初步认识
+ [python100语感][python100]来自天元浪子的python语感训练

# Iterator
:rocket:[click here](/Iterator/README.md)

主要介绍`可迭代对象(Iterable)`、`迭代器(Iterator)`和`生成器(Generator)`。

迭代是数据处理极其重要的部分，我们处理内存中放不下的数据时，我们需要一种惰性地处理方式，按需一次获取一个数据项。这带来的好处是在数据处理的过程中降低内存的使用(数据按需获取！)。

主要学习
- 使用Python实现经典的迭代器
- 说明生成器的工作原理
- 使用yield from 合并生成器
- 可迭代对象，迭代器，生成器之间的关系

# Closure
闭包, 实现装饰器的基础。除此之外闭包还是回调异步编程和函数式编程的基础。

主要学习
- Python如何计算装饰器语法
- Python如何判断变量是不是局部的
- 闭包存在的原因和工作原理
- nonlocal能解决什么问题

在这个基础上我们深入讨论装饰器
- 实现行为良好的装饰器
- 标准库中有用的装饰器
- 实现一个参数化的装饰器

# MultiThread
多线程

# MultiProcessing
多进程

# Coroutine
协程

---
[tutorial]: https://nbviewer.jupyter.org/github/codebysandwich/Python_Core/blob/master/Foundation/Tutorial.ipynb

[python100]: https://github.com/codebysandwich/Python_Core/blob/master/Foundation/python100%E8%AF%AD%E6%84%9F.md
