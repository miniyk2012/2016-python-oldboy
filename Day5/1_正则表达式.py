# -*- coding:utf-8 -*-

import re
string = "alex Li afs lkjkalex hi i"
print(re.findall("^a.*i$", string, re.M))

string = "alex Li afs lkji\nakalex hi i"
print(re.findall("^a.*i$", string, re.M))
print(re.findall("(.|\s)*", string))    # 最终也没怎么理解

