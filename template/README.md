# Introduction

## Library Function

```python
import os, sys, random

# sys.exit() 退出程序
# sys.setrecursionlimit(10**6) #调整栈空间
from sys import stdin, stdout, setrecursionlimit

# randint(a,b)从[a,b]范围随机选择一个数
# choice(seq)seq可以是一个列表,元组或字符串,从seq中随机选取一个元素
# shuffle(x)将一个可变的序列x中的元素打乱
from random import randint, choice, shuffle

from copy import deepcopy
from io import BytesIO, IOBase
from types import GeneratorType

# reduce(op, 迭代对象)
from functools import lru_cache, reduce

# bisect_left(x) 大于等于x的第一个下标
# bisect_right(x) 大于x的第一个下标
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque

# accumulate(a) 用a序列生成一个累积迭代器，一般list化前面放个[0]做前缀和用
# combinations(a,k) a序列选k个组合迭代器
# permutations(a,k) a序列选k个排列迭代器
from itertools import accumulate, combinations, permutations

# heapify将列表转为堆
from heapq import heapify, heappop, heappush
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

# 小写字母，大写字母，十进制数字
from string import ascii_lowercase, ascii_uppercase, digits

# ceil向上取整，floor向下取整，sqrt开方，factorial阶乘
from math import ceil, floor, sqrt, isqrt, factorial, gcd, log, log10, log2, pi, inf

# Decimal(s) 实例化Decimal对象,一般使用字符串
# getcontext().prec=100 修改精度
from decimal import Decimal, getcontext
```
