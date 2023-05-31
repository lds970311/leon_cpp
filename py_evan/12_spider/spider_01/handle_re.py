# coding:utf-8
# time: 2023/5/30
# author: evan

import re

pattern = re.compile(r'\d+')
match = pattern.match('one12twothres123', 3)
print(match.group())

all = pattern.findall('one12twothres123')
print(all)

pattern = re.compile(r'[\s\,\;]+')
match = pattern.split('a,b;; c  d')
print(match)  # ['a', 'b', 'c', 'd']
