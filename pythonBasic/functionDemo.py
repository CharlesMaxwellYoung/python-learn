from collections import Iterable
import os


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('demo', 30, demo='demo', demo1='2')


def move(n, a, b, c):
    if n == 1:
        print('move', a, '--->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(2, 'A', 'B', 'C')

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])
# 前三个数
print(L[:3])
# 后三个数
print(L[-3:])
# 前10个数，每两个取一个：
print(L[:10:2])
# 所有数，每5个取一个：
print(L[::5])
# 只写[:]就可以原样复制一个list：
print(L[:])

T = (0, 1, 2, 3, 4, 5)
print(T[:3])

print('ABCDEFG'[:3])

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

print(isinstance('abc', Iterable))

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：

print(list(range(1, 10)))

# [1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
print([x * x for x in range(1, 1000)])

# 顺便筛选出偶数
print([x * x for x in range(1, 11) if x % 2 == 0])

# 使用两层循环，可以生成全排列：
print([m + x for m in 'ZXC' for x in 'YUI'])

print([d for d in os.listdir('.')])

X = ['Hello', 'World', 18, 'Apple', None]

print([x.lower() for x in X if isinstance(x, str)])

# 生成器,直接将列表生成[]---->()
g = (x * x for x in range(10))
print(next(g))


# 斐波拉契数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'none'


# 将上面函数变成generator
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'none'


print(fib(3))
print(next(fib1(5)))


def triangles():
    n, a, b = 0, 0, 1
    
