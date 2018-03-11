# 字符编码
# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
print('包含中文的str')

print('\u4e2d\u6587')

print('中文'.encode('utf-8'))
print(len('包含中文的str'))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

a = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.2225)

print(a)

# list和tuple

classmates = ['one ', 'two', 'thee']

print(classmates)

print(len(classmates))

classmates.insert(1, 'dd')
classmates.append('c')
classmates.pop(1)

print(classmates)

# 元组

t = (1,)
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

# 条件语句
age = 3
if age > 3:
    print('a')
elif age > 4:
    print('b')
else:
    print('c')


def BMI(height, weight):
    height = float(height)
    weight = float(weight)
    bmi = weight / (height * height)
    bmi = float(bmi)
    if bmi < 18.5:
        print('过轻')
    elif 25 >= bmi >= 18.5:
        print('正常')
    elif 28 >= bmi >= 25:
        print('过重')
    elif 32 >= bmi >= 28:
        print('正常')
    else:
        print('严重肥胖')


height = 1.75
weight = 80
BMI(height, weight)

# 循环
# Python的循环有两种，一种是for...in循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in range(101):
    sum += x
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环
L = ['Bart', 'Lisa', 'Adam']

for item in L:
    print(item)
n = 1
while n <= len(L):
    print(L[n - 1])
    n += 1

# dict 相当于其他语言的map类型
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('d' in d)

a1 = ['c', 'b', 'a']
a1.sort()
print(a1)

