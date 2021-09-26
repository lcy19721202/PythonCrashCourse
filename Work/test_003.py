#!/opt/local/bin/python
# -*- coding: utf-8 -*-

# 列表创建与删除

a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
print(a_list)

a_list = []  # 创建空列表
print(a_list)

# 使用list()函数创建列表

a_list = list((3, 5, 7, 9, 11))
print(a_list)
a_list.append(13)
print(a_list)

x = list(range(1, 10, 2))
print(x)
x = list('hello world')
print(x)
x = list()  # 创建空列表
print(x)

del x
