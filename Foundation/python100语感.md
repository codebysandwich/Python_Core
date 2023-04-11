# python 100道语感练习

1. 将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表
   
```python
list((1, 2, 3)) + list({4, 5, 6})
>>>[1, 2, 3, 4, 5, 6]
```

2. 在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0
   
```python
l = [1, 2, 3, 4, 5, 6]
l.insert(0, 7)
l.append(0)
l
>>>[7, 1, 2, 3, 4, 5, 6, 0]
```

3. 反转列表 [0,1,2,3,4,5,6,7]

```python
# 解法1
l = [0,1,2,3,4,5,6,7]
l.reverse()
l
>>>[7, 6, 5, 4, 3, 2, 1, 0]
# 解法2
l = [0,1,2,3,4,5,6,7]
list(reversed(l))
>>>[7, 6, 5, 4, 3, 2, 1, 0]
```

4. 反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号

```python
list(reversed([0,1,2,3,4,5,6,7])).index(5)
>>>2
```

5. 分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？

```python
l = [True,False,0,1,2] 
l.count(True)
>>>2
l.count(False)
>>>2
l.count(0)
>>>2
l.count(1)
>>>2
l.count(2)
>>>1
```

对于这部分的理解和解释，请看：
```python
1 == True, 0 == False
>>>(True, True)
```

6. 从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’
   
```python
l = [True, 1, 0, 'x', None, 'x', False, 2, True]
l = list(filter(lambda s: s!='x', l))
l
>>>[True, 1, 0, None, False, 2, True]
```

7. 从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为4的元素

```python
# 解法1
l = [True, 1, 0, 'x', None, 'x', False, 2, True]
del(l[4])
l
>>>[True, 1, 0, 'x', 'x', False, 2, True]
# 解法2， 附带取出删除的元素的功能
l = [True, 1, 0, 'x', None, 'x', False, 2, True]
l.pop(4)
l
>>>[True, 1, 0, 'x', 'x', False, 2, True]
```

8. 删除列表中索引号为奇数（或偶数）的元素

```python
l = list(range(10))
del l[::2]
l
>>>[1, 3, 5, 7, 9]
l = list(range(10))
del l[1::2]
l
>>>[0, 2, 4, 6, 8]
```

9. 清空列表中的所有元素

```python
l = [1, 5, 6]
l.clear()
l
>>>[]
```

友情提示： 清空列表不等于删除列表

10. 对列表 [3,0,8,5,7] 分别做升序和降序排列

```python
l = [3,0,8,5,7]
# 升序排序
l.sort()
l
>>>[0, 3, 5, 7, 8]
l = [3,0,8,5,7]
# 降序
l.sort(reverse=True)
l
>>>[8, 7, 5, 3, 0]
```

11. 将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0
    
```python
l = [3,0,8,5,7]
list(map(lambda s: 1 if s>5 else 0, l))
>>>[0, 0, 1, 0, 1]
```

12. 遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号

```python
l = ['x', 'y', 'z']
for index, val in enumerate(l):
    print(index, val)
>>>0 x
1 y
2 z
```

13. 将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表

```python
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b = l[::2], l[1::2]
a
>>>[0, 2, 4, 6, 8]
b
>>>[1, 3, 5, 7, 9]
```

14. 分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序

```python
l = [[6, 5], [3, 7], [2, 8]]
list(sorted(l, key=lambda s: (s[0], s[-1])))
>>> [[2, 8], [3, 7], [6, 5]]
```

15. 从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素

```python
l = [1,4,7,2,5,8]
for i, val in enumerate(['x', 'y', 'z']):
    l.insert(3+i, val)
l
>>>[1, 4, 7, 'x', 'y', 'z', 2, 5, 8]
```

16. 快速生成由[5, 50)区间内的整数组成的列表

```python
list(range(5, 50))
>>>[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
```

17. 若 a = [1,2,3]，令 b = a，执行 b[0] = 9， a[0]亦被改变。为何？如何避免？
    
```python
# b=a 执行浅拷贝
# 用copy实现
a = [1, 2, 3]
b = a.copy()
b[0] = 9
a
>>>[1, 2, 3]
```

18. 将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式。
    
```python
list(zip(['x', 'y', 'z'], [1, 2, 3]))
>>>[('x', 1), ('y', 2), ('z', 3)]
```

19. 以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键。

```python
kv = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
kv.keys()
>>>dict_keys(['Alice', 'Beth', 'Cecil'])
# 列表表达式完成
[k for k in kv]
>>>['Alice', 'Beth', 'Cecil']
```

20. 以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值。

```python
kv = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
kv.values()
>>>dict_values([20, 18, 21])
[v for v in kv.values()]
>>>[20, 18, 21]
```

21. 以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组。
```python
kv = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
kv.items()
>>>dict_items([('Alice', 20), ('Beth', 18), ('Cecil', 21)])
[(k, v) for k, v in kv.items()]
>>> [('Alice', 20), ('Beth', 18), ('Cecil', 21)]
```

22. 向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17。
```python
kv = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
kv['David'] = 19
kv['Cecil'] = 17
kv
>>>{'Alice': 20, 'Beth': 18, 'Cecil': 17, 'David': 19}
```

23. 删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典。
```python
kv = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
kv.pop('Beth') # 可以用del kv['Beth']实现
>>>18
kv
>>> {'Alice': 20, 'Cecil': 21}
kv.clear()
kv
>>>{}
```

24. 判断 David 和 Alice 是否在字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中。
```python
kv = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
'David' in kv
>>>False
'Alice' in kv
>>>True
```

25. 遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对。
```python
kv = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
for k, v in kv.items():
    print('{}: {}'.format(k, v))
>>>Alice: 20
Beth: 18
Cecil: 21
```

26. 若 a = dict()，令 b = a，执行 b.update({‘x’:1})， a亦被改变。为何？如何避免？
```python
# python 默认浅拷贝
a = dict()
b = a
b.update({"x": 1})
a
>>>{'x': 1}
a = dict()
b = a.copy()
b.update({"x": 1})
a
>>>{}
```

27. 以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典。
```python
l = list('ABCDEFGH')
dict.fromkeys(l, 0)
>>> {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
```

28. 将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典。
```python
# dict官档中生成字典的一种方式
# dict(iterable) -> new dictionary initialized as if via:
#     d = {}
#     for k, v in iterable:
#         d[k] = v
arr = [['a', 1], ['b', 2]]
dict(arr)
>>>{'a': 1, 'b': 2}
ts = (('x', 3), ('y', 4))
dict(ts)
>>>{'x': 3, 'y': 4}
```

29. 将元组 (1,2) 和 (3,4) 合并成一个元组。
```python
# 元组不可修改，+计算实现
t1 = (1, 2)
t2 = (3, 4)
t1 + t2
>>> (1, 2, 3, 4)
```

30. 将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z。
```python
x, y, z = *(1, 2, 3)
x
>>>1
```

31. 返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号。
```python
t = ('Alice', 'Beth', 'Cecil')
t.index('Cecil')
>>>2
```

32. 返回元组 (2,5,3,2,4) 中元素 2 的个数。
```python
t = (2,5,3,2,4)
t.count(2)
>>>2
```

33. 判断 ‘Cecil’ 是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中。
```python
t = ('Alice', 'Beth', 'Cecil')
'Cecil' in t
>>>True
```
34. 返回在元组 (2,5,3,7) 索引号为2的位置插入元素 9 之后的新元组。
```python
# 元组无法修改， 借助列表实现
t = (2,5,3,7)
l = list(t)
l.insert(2, 9)
tuple(l)
>>> (2, 5, 9, 3, 7)
```

35. 创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。
```python
s = set()  # 创建空集合
s.union({'x', 'y', 'z'}) # 并集计算得到新的集合， s不变
>>>{'x', 'y', 'z'}
for ele in {'x', 'y', 'z'}:
    s.add(ele)
s
>>>{'x', 'y', 'z'}
```

36. 删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增j加元素 ‘w’，然后清空整个集合。
```python
s = {'x', 'y', 'z'}
s.remove('z')
s
>>>{'x', 'y'}
s.add('w')
s
>>>{'w', 'x', 'y'}
s.clear()
s
>>>set()
```

37. 返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）。
```python
s1 = {'A', 'D', 'B'}
s2 = {'D', 'E', 'C'}
s1 - s2
>>>{'A', 'B'}
s1.difference(s2)
>>>{'A', 'B'}
```

38. 返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集。
```python
s1 = {'A', 'D', 'B'}
s2 = {'D', 'E', 'C'}
s1.union(s2)
>>>{'A', 'B', 'C', 'D', 'E'}
s1 | s2  # 位操作符实现
>>>{'A', 'B', 'C', 'D', 'E'}
```

39. 返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集。
```python
s1 = {'A', 'D', 'B'}
s2 = {'D', 'E', 'C'}
s1.intersection(s2)
>>>{'D'}
s1 & s2
>>>{'D'}
```

40. 返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合。

```python
s1 = {'A', 'D', 'B'}
s2 = {'D', 'E', 'C'}
s1.symmetric_difference(s2)
>>>{'A', 'B', 'C', 'E'}
s1 & s2
(s1 | s2) - (s1 & s2)
>>>{'A', 'B', 'C', 'E'}
```

41. 判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素。
```python
s1 = {'A', 'D', 'B'}
s2 = {'D', 'E', 'C'}
s1 & s2 != set()
>>>True
```

42. 判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集。
    
```python
s1 = {'A', 'C'}
s2 = {'D', 'C', 'E', 'A'}
s1.issubset(s2)
>>>True
```

43. 去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素。

```python
l = [1,2,5,2,3,4,5,'x',4,'x']
list(set(l))
>>>[1, 2, 3, 4, 5, 'x']
```

44. 返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大小写互换形式。

```python
s = 'abCdEfg'
s.upper()
>>>'ABCDEFG'
s.lower()
>>>'abcdefg'
s.swapcase()
>>>'ABcDeFG'
```

45. 判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写。

```python
s = 'abCdEfg'
s.istitle()   # 这个例子我觉得有点问题
>>>False
s.islower()
>>>False
s.isupper()
>>>False
```

46. 返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式。
    
```python
s = 'this is python'
s.capitalize()
>>>'This is python'
s.title()
>>>'This Is Python'
>>>
```

47. 判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾。

```python
s = 'this is python'
s.startswith('this')
>>>True
s.endswith('python')
>>>True
```

48. 返回字符串 ‘this is python’ 中 ‘is’ 的出现次数。

```python
s = 'this is python'
s.count('is')
>>>2
```

49. 返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置。

```python
s = 'this is python'
s.index('is')
>>>2
s.rfind('is')
>>>5
```

50. 将字符串 ‘this is python’ 切片成3个单词。

```python
s = 'this is python'
s.split()
>>>['this', 'is', 'python']
```

51. 返回字符串 ‘blog.csdn.net/xufive/article/details/102946961’ 按路径分隔符切片的结果。

```python
s = 'blog.csdn.net/xufive/article/details/102946961'
s.split('/')
>>> ['blog.csdn.net', 'xufive', 'article', 'details', '102946961']
```

52. 将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形。

```python
s = '2.72, 5, 7, 3.14'
[int(item) if item.isdigit() else float(item) for item in s.split(', ')]
>>>[2.72, 5, 7, 3.14]
```
53. 判断字符串 ‘adS12K56’ 是否完全为字母数字，是否全为数字，是否全为字母，是否全为ASCII码。

```python
s = 'adS12K56'
s.isalnum()
>>>True
s.isdigit()
>>>False
isascii = lambda s: all(ord(c) < 128 for c in s)
isascii(s)
>>>True
```

54. 将字符串 ‘there is python’ 中的 ‘is’ 替换为 ‘are’。

```python
'there is python'.replace('is', 'are')
>>>'there are python'
```

55. 清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符。

```python
s = '\t python \n'
s.lstrip()
>>>'python \n'
s.rstrip()
>>>'\t python'
s.strip()
>>>'python'
```
56. 将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果。

```python
ls = ['ok', 'hello', 'thank you']
for item in ls:
    print('{:<10s}'.format(item))
>>>
'ok'
'hello'
'thank you'
for item in ls:
    print('{:>10s}'.format(item))
>>>
'        ok'
'     hello'
' thank you'
for item in ls:
    print('{:^10s}'.format(item))
>>>
'    ok   '
'  hello  '
'thank you'

# 函数实现
for item in ls:
    print('%s' % item.rjust(10))
>>>
'        ok'
'     hello'
' thank you'
```

57. 将三个字符串（比如，‘Hello, 我是David’, ‘OK, 好’, ‘很高兴认识你’）分行打印，实现左对齐、右对齐和居中效果。

```python
### 同上
```

58. 将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补0成同样长度。

```python
ls = ['15', '127', '65535']
num = max(len(item) for item in ls)
for item in ls:
    print('%s' % item.zfill(num))
>>>
'00015'
'00127'
'65535'
# 倔强地使用format
fmt = '{:0>%ds}' % num
for item in ls:
    print(fmt.format(item))
>>>
'00015'
'00127'
'65535'
```

59. 提取 url 字符串 ‘https://blog.csdn.net/xufive’ 中的协议名。

```python
'https://blog.csdn.net/xufive'.split('//')[0][:-1]
>>>'https'
```

60. 将列表 [‘a’,‘b’,‘c’] 中各个元素用’|'连接成一个字符串。

```python
l = ['a', 'b', 'c']
'|'.join(l)
>>>'a|b|c'
```

61. 将字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串。

```python
','.join(list('abc'))
>>>'a,b,c'
```

62. 从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串。

```python
s = input(">>>输入手机号")
print('Mobiel: {:3s} {:4s} {:4s}'.format(s[:3], s[3:6], s[6:]))

>>>'Mobiel: 186 667  77788'
```

63. 从键盘输入年月日时分秒，输出形如 ‘2019-05-01 12:00:00’ 的字符串。

```python
# 键盘上输入的结果都记录为字符串
year = input("请输入年份：")
month = input("请输入月份：")
day = input("请输入日：")
hour = input("请输入小时：")
minute = input("请输入分钟：")
second = input("请输入秒：")
fmt = '{:4s}-{:0>2s}-{:0>2s} {:0>2s}:{:0>2s}:{:0>2s}'
print(fmt.format(year, month, day, hour, minute, second))
>>>'2019-05-01 12:00:00'
```

64. 给定两个浮点数 3.1415926 和 2.7182818，格式化输出字符串 ‘pi = 3.1416, e = 2.7183’。

```python
pi = 3.1415926
e = 2.7182818
print('pi = %.4f, e = %.4f' % (pi, e))
>>>'pi = 3.1416, e = 2.7183'
# 用format实现
fmt = 'pi = {:.4f}, e = {:.4f}'
print(fmt.format(pi, e))
>>>'pi = 3.1416, e = 2.7183'
```

65. 将 0.00774592 和 356800000 格式化输出为科学计数法字符串。

```python
x = 0.00774592
print("%.2e" % x)
>>>'7.75e-03'
y = 356800000
# 稍微花式的实现方法
print(f'{y:.2E}')
>>>'3.57E+08'
```

66. 将十进制整数 240 格式化为八进制和十六进制的字符串。

```python
x = 240
# 转8进制
print('%o' % x)
>>>360
# 转化16进制
print('{:X}'.format(x))
>>>'F0'
```

67. 将十进制整数 240 转为二进制、八进制、十六进制的字符串。

```python
print('{:b}'.format(240))
>>>'11110000'
print(oct(240))
>>>'0o360'
print(hex(240))
>>>'0xf0'
```

68. 将字符串 ‘10100’ 按照二进制、八进制、十进制、十六进制转为整数。

```python
s = '10100'
print(int(s, base=2))
>>>20
print(int(s, base=8))
>>>4160
print(int(s, base=16))
>>>65792
```

69. 求二进制整数1010、八进制整数65、十进制整数52、十六进制整数b4的和。

```python
0b1010 + 0o65 + 52 + 0xb4
>>>295
```

70. 将列表 [0,1,2,3.14,‘x’,None,’’,list(),{5}] 中各个元素转为布尔型。

```python
l = [0,1,2,3.14,'x',None,'',list(),{5}]
[bool(item) for item in l]
>>> [False, True, True, True, True, False, False, False, True]
```

71. 返回字符 ‘a’ 和 ‘A’ 的ASCII编码值。

```python
ord('a'), ord('A')
>>>(97, 65)
```

72. 返回ASCII编码值为 57 和 122 的字符。

```python
chr(57), chr(122)
>>> ('9', 'z')
```

73. 将二维列表 [[0.468,0.975,0.446],[0.718,0.826,0.359]] 写成名为 csv_data 的 csv 格式的文件，并尝试用 excel 打开它。

```python
l = [[0.468,0.975,0.446],[0.718,0.826,0.359]]
with open(r'D:\csv_data.csv', 'a+') as f:
    for row in l:
        f.write(','.join([str(item) for item in row])+'\n')
```

74. 从 csv_data.csv 文件中读出二维列表。

```python
res = []
with open(r'D:\csv_data.csv', 'r') as f:
    for line in f.readlines():
        res.append([float(item) for item in line.strip().split(',')])
res
>>>[[0.468, 0.975, 0.446], [0.718, 0.826, 0.359]]
```

75. 向 csv_data.csv 文件追加二维列表 [[1.468,1.975,1.446],[1.718,1.826,1.359]]，然后读出所有数据。

```python
l = [[1.468,1.975,1.446],[1.718,1.826,1.359]]
with open(r'D:\csv_data.csv', 'a+') as f:
    for row in l:
        f.write(','.join([str(item) for item in row])+'\n')
```

76. 交换变量 x 和 y 的值。

```python
a = 1
b = 2
a, b = b, a
a
>>>2
b
>>>1
```

77. 判断给定的参数 x 是否是整形。

```python
x = 123
isinstance(x, int)
>>>True
```

78. 判断给定的参数 x 是否为列表或元组。

```python
l = []
t = (1, )
isinstance(l, (list, tuple))
>>>True
isinstance(t, (list, tuple))
>>>True
```

79. 判断 ‘https://blog.csdn.net’ 是否以 ‘http://’ 或 ‘https://’ 开头。若是，则返回 ‘http’ 或 ‘https’；否则，返回None。

```python
url = 'https://blog.csdn.net'
def get_start(string, start):
    if string.startswith(start):
        return string.split(':')[0]
print(get_start(url, 'http://'))
>>>None
get_start(url, 'https://')
>>>'https'
```

80. 判断 ‘https://blog.csdn.net’ 是否以 ‘.com’ 或 ‘.net’ 结束。若是，则返回 ‘com’ 或 ‘net’；否则，返回None。

```python
url = 'https://blog.csdn.net'
def get_end(url, part):
    if url.endswith(part):
        return url.split('.')[-1]
print(get_end(url, '.com'))
>>>None
get_end(url, '.net')
>>>'net'
```
+ python 中函数进入没有返回时，函数自动返回None, 或者说函数默认返回None。从函数设计的角度上来说我们应该确保所有情况都有返回！

81. 将列表 [3,‘a’,5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0。

```python
l = [3,'a',5.2,4,{},9,[]]
def map_func(s):
    if isinstance(s, (int, float)):
        return 1 if s > 3 else 0
    else:
        return 0
list(map(map_func, l))
>>>[0, 0, 1, 1, 0, 1, 0]
# 列表表达式实现
[1 if isinstance(item, (float, int)) and item > 3  else 0 for item in l]
>>>[0, 0, 1, 1, 0, 1, 0]
```
+ 注意isinstance(item, (float, int))在前，这是逻辑的先后技巧！

82. a,b 是两个数字，返回其中较小者或最大者。

```python
a, b = 3, -9
a if a > b else b
>>>3
```

83. 找到列表 [8,5,2,4,3,6,5,5,1,4,5] 中出现最频繁的数字以及出现的次数。

```python
from collections import Counter
l = [8,5,2,4,3,6,5,5,1,4,5]
count = Counter(l)
key, c = count.most_common(1)[0]
key, c
>>>(5, 4) # 5最多出现4次
# max技巧， 按照条件（l中的计数值）获取最大值
max(set(l), key=l.count)
>>>5
l.count(5)
>>>4
```

84. 将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为 一维列表。

```python
l = [[1], ['a', 'b'], [2.3, 4.5, 6.7]]
# 利用list可以相加的特点，注意初始化[]， 默认0，0不能和list相加
sum(l, [])
>>>[1, 'a', 'b', 2.3, 4.5, 6.7]
```

85. 将等长的键列表和值列表转为字典。

```python
k = ['a', 'b', 'c']
v = [1, 2, 3]
dict(zip(k, v))
>>>{'a': 1, 'b': 2, 'c': 3}
```

86. 使用链状比较操作符重写逻辑表达式 a > 10 and a < 20。

```python
a = 12
10 < a < 20
>>>True
```

87. 写一个函数，以0.1秒的间隔不换行打印30次由函数参数传入的字符，实现类似打字机的效果。

```python
from time import sleep
def printer(ch, timer, count):
    for i in range(count): # 打印 30次
        print(ch, end='') # 打印*， 不换行
        sleep(timer) # 延时0.1秒
printer('*', 0.1, 30)
>>>******************************
```

88. 数字列表求和。

```python
sum([1, 3, 4])
>>>8
```

89. 返回数字列表中的最大值和最小值。

```python
l =[1, 5, 6, 2, 5] 
max(l), min(l)
>>> (6, 1)
```

90. 计算 5 的 3.5 方和 3 的立方根。

```python
pow(5, 3.5), pow(5, 3)
>>>(279.5084971874737, 125)
```

91. 对 3.1415926 四舍五入，保留小数点后5位。

```python
round(3.1415926, 5)
>>>3.14159
```
+ 小心浮点数精度，四舍六入五成双要小心

92. 判断两个对象是在内存中是否是同一个。

```python
a = b = 34
a is b
>>>True
```

93. 返回给定对象的属性和方法。

```python
a = ()
for item in dir(a):
    print(item)
>>>
__add__
__class__
__contains__
__delattr__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__getnewargs__
__gt__
__hash__
__init__
__init_subclass__
__iter__
__le__
__len__
__lt__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__rmul__
__setattr__
__sizeof__
__str__
__subclasshook__
count
index
```

94. 计算字符串表达式 ‘(2+3)*5’ 的值。

```python
eval('(2+3)*5')
>>>25
```
+ 结合__repr__理解

95. 实现字符串 ‘x={“name”:“David”, “age”:18}’ 包含的代码功能。

```python
exp = "x={'name':'David', 'age':18}"
exec(exp)
x
>>>{'name': 'David', 'age': 18}
```

96. 使用 map 函数求列表 [2,3,4,5] 中每个元素的立方根。

```python
list(map(lambda s: pow(s, 3), [2,3,4,5]))
>>> [8, 27, 64, 125]

[item for item in map(lambda s: pow(s, 3), [2,3,4,5])]
>>>[8, 27, 64, 125]
```

97. 使用 sys.stdin.readline() 写一个和 input() 函数功能完全相同的函数。

```python
import sys
def my_input(prompt):
    print(prompt, end='')
    return sys.stdin.readline().strip()
my_input("请输入：")
>>>请输入：23
'23'
```

98. 使用二维列表描述9x9围棋局面，'w’表示白色棋子，‘b’表示黑色棋子，’-'表示无子，打印成下图左所示的文本棋盘。

```python
# 输入时学会偷懒
phase = [['-']*9,
         ['-']*9,
         ['-']*2+['w']+['-']*3+['b']+['-']*2,
         ['-']*9,
         ['-']*4+['b']+['-']*4,
         ['-']*9,
         ['-']*2+['w']+['-']*3+['b']+['-']*2,
         ['-']*9,
         ['-']*9
         ]
print('+'+'-'*19+'+')
for row in phase:
    print('| %s |' % ' '.join(row))
print('+'+'-'*19+'+')
>>>
+-------------------+
| - - - - - - - - - |
| - - - - - - - - - |
| - - w - - - b - - |
| - - - - - - - - - |
| - - - - b - - - - |
| - - - - - - - - - |
| - - w - - - b - - |
| - - - - - - - - - |
| - - - - - - - - - |
+-------------------+
```

99.  对于9x9围棋盘，用a-i标识各行，用1-9标识各列，设计函数go()，输入位置和颜色，即输出文本棋盘，模拟围棋对弈的过程。

```python
phase = [['-']*9 for i in range(9)]
def go(row, col, c):
    row = ord(row) - ord('a')
    col -= 1
    phase[row][col] = c
    print('+'+'-'*19+'+')
    for line in phase:
        print('| %s |' % ' '.join(line))
    print('+'+'-'*19+'+')

go('c', 7, 'b')
>>>
+-------------------+
| - - - - - - - - - |
| - - - - - - - - - |
| - - - - - - b - - |
| - - - - - - - - - |
| - - - - - - - - - |
| - - - - - - - - - |
| - - - - - - - - - |
| - - - - - - - - - |
| - - - - - - - - - |
+-------------------+

go('g', 3, 'w')
>>>
+-------------------+
| - - - - - - - - - |
| - - - - - - - - - |
| - - - - - - b - - |
| - - - - - - - - - |
| - - - - - - - - - |
| - - - - - - - - - |
| - - w - - - - - - |
| - - - - - - - - - |
| - - - - - - - - - |
+-------------------+

go('g', 7, 'b')
>>>
+-------------------+
| - - - - - - - - - |
| - - - - - - - - - |
| - - - - - - b - - |
| - - - - - - - - - |
| - - - - - - - - - |
| - - - - - - - - - |
| - - w - - - b - - |
| - - - - - - - - - |
| - - - - - - - - - |
+-------------------+
```

+ 这不能算是一个游戏， 对于新手来说还是可以磨练基本功的。

100. 下图中是国际跳棋的初始局面，10x10的棋盘上只有50个深色格子可以落子，'w’表示白色棋子，‘b’表示黑色棋子，’-'表示无子，字符串 phase = ‘b’*20 + ‘-’*10 + ‘w’*20 表示下图中的局面，请将 phase 打印成下图右所示的样子。

```python
phase = 'b'*20 + '-'*10 + 'w'*20 # 50个字符
# 分析-每行字符个数一致 == 5， 空格一致==16， 每行错位而已
print('+ '+'- '*10+'+')
for i in range(10):
    # 取出字符
    chs = phase[i*5:(i+1)*5]
    # 填充空格
    lin = '   '.join(list(chs))
    if i % 2 == 0:
        print('|   '+lin+' |')
    else:
        print('| '+lin+'   |')
print('+ '+'- '*10+'+')
>>>
+ - - - - - - - - - - +
|   b   b   b   b   b |
| b   b   b   b   b   |
|   b   b   b   b   b |
| b   b   b   b   b   |
|   -   -   -   -   - |
| -   -   -   -   -   |
|   w   w   w   w   w |
| w   w   w   w   w   |
|   w   w   w   w   w |
| w   w   w   w   w   |
+ - - - - - - - - - - +
```


![image][1]















[1]: https://img-blog.csdnimg.cn/20191113093308937.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1Zml2ZQ==,size_16,color_FFFFFF,t_70
