# -*- coding:utf-8 -*-
import re

p = re.compile('[a-z]+')  # p是一个_sre.SRE_Pattern
print(type(p))
m = p.match("tempo")    # m是一个# _sre.SRE_Match object
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

print(''.center(50, '-'))
s = p.search('::: message')     # s是一个# _sre.SRE_Match object
print(s)
print(s.span())
print(s.group())

print(''.center(50, '-'))
p = re.compile('[a-z]+')
m = p.match('string goes here')
if m:
    print('Match found: ', m.group())
else:
    print('No match')

print(''.center(50, '-'))
p = re.compile(r'\d+')
f = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
print(f)

iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
print(iterator)
for match in iterator:
    print(match)    # match是一个_sre.SRE_Match object
    print(match.span(), match.group())

m = re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
print(m)
print(m.span(), m.group())

s = re.search('}$', '{block}')
print(s.group())

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

print(50*'-')
p = re.compile('(ab)*')
m = p.match('ababababab')
print(m)
print(m.group(0,1))
print(m.span(1))

print(50*'-')
p = re.compile('(a(b)c)d')
m = p.match('abcd')
print(m.span(2))
print(m.groups())  # The groups() 方法返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())

m = re.match("(?:[abc])+", "abc")
print(m.groups())

print(50*'-')
p = re.compile(r'(?P<word>\b\w+\b)')
m = p.search( '(((( Lots of punctuation )))' )
print(m.group(1))
print(m.group('word'))

print(50*'-')
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
s = p.search('Paris in the the spring')
print(s.group())
print(s.groups())

print(50*'-')
phone_str = "hey my name is alex, and my phone number is 13651054607, please call me if you are pretty!"
phone_str2 = "hey my name is alex, and my phone number is 18651054604, please call me if you are pretty!"
m = re.search("(1)([358]\d{9})",phone_str2)
if m:
    print(m.group())

print('计算器'.center(50, '-'))
val = '9-2*-5/3 + 7 /3*99/4*2998 +10 * 568/14'
mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val)
print(mch.group())

val = '1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', val).group()
print(content)