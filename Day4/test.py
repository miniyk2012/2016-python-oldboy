# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
import re

temp = "jk中文 -123456aa哈哈哈bbcc".decode('utf8')
# s='jkjkl中文：123456aa哈哈哈bbcc'.decode('utf8')
# result = re.search('([^\w\s]+)|(u"[^\u4e00-\u9fa5]+)', temp)
result = re.search(u'([^\u4e00-\u9fa5\w\s]+)', temp)
if result:
    print('hah')
    print(result.group())

# print(re.search(u"[\u4e00-\u9fa5]+",s).group())

