# -*- coding:utf-8 -*-

import re


pattern = r"\\section"
string = '\sectionxu'
m = re.match(pattern, string, re.IGNORECASE)
print(m)
print(m.group())

pattern = '[0-9]+'
m = re.match(pattern, 'u8us78jkjk')  # match只能从头开始匹配
if m:
    print(m.group())



pattern = '[0-9]{0,10}'
m = re.findall(pattern, 'u8us78jkjk')
print(m)

pattern = '[a-zA-Z]{1,10}'
m = re.findall(pattern, 'u8us78jkjk')
print(m)

pattern = '\w+'
m = re.findall(pattern, 'u8us7@#8jkjk')
print(m)

pattern = '\w+'
m = re.findall(pattern, 'u8us7@#8jkjk')
print(m)

pattern = '\d+'
m = re.search(pattern, 'u8us7@#8jkjk')  # search返回第一个找到的
print(m)
if m:
    print(m.group())

pattern = '\d+'
m = re.sub(pattern, '|', 'u8us7@#8jkjk', count=2)
print(m)

