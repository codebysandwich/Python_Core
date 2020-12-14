# 闭包与装饰器

## 装饰器基础
装饰器是可调用的对象，调用对象是被装饰的函数。可以对被装饰的函数处理之后返回，也可以将其替换成另一个函数或可调用对象。-这里揭示了一个潜在的容易被忽略的问题，被装饰器装饰过后的函数已经不再是原来的函数了。

```python
def deco(func):
    def inner():
        print("running inner()")
    return inner

@deco
def target():
    print("running target()")


if __name__ == "__main__":
    target()
```
```
>>> running inner()
```
这里我们直接将target函数替换了,可以看到deco中只是接收了target,返回的是inner。所以说装饰器会将被装饰的函数替换(修改),以此达到增加功能的目的。同时这也揭露了一个事实，装饰器是可调用的，上面的写法等价于：
```python
def targrt():
	print("running targrt()")

targrt = deco(targrt)
targrt()

>>>running inner()
```
同样的原target函数被装饰后进行了同名替换。

## python何时执行装饰器
另一个重要的特性-被装饰函数定义时运行装饰器,
