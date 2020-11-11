import os
from collections import Iterator

# 循环
# for in 和 while
needSum = 0
n = 99
while n > 0:
    needSum = needSum + n
    n = n - 2
print(needSum)

forSum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    forSum = forSum + x
else:
    print(forSum)

print(forSum)

# 分片：step省略默认为1，start为下标开始，stop为下标结束
# list[start:stop:step]

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L), print(len(L))
print(L[:25])
print(L[-25:])
r = list(range(100, 0, -10))
print(r)

# 迭代 for in
for i in L[1:3]:
    print(i)

# list 生成式
newList1 = [x for x in range(1, 11)]
newList = [x * x for x in range(1, 11)]
oddList1 = [x for x in range(1, 11) if x % 2 == 0]
oddList = [x * x for x in range(1, 11) if x % 2 == 0]
twoForLevelList = [m + n for m in 'ABC' for n in 'XYZ']

files = [d for d in os.listdir('.')]  # listdir 中的参数是要列出文件的路径
print(files)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
# 生成器generator
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
g = (x * x for x in range(10))
next(g)  # generator可以调用next

tt = (1, "hello")
print("tuple factor")
for i in tt:
    print(i)
firstFactor = tt[0]
secondFactor = tt[1]
print(firstFactor), print(secondFactor)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


ne = odd()
print(next(ne))
print(next(ne))
print(next(ne))


isinstance('abc', Iterator)
isinstance(iter('abc'), Iterator)
