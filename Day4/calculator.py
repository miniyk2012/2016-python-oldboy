# -*- coding:utf-8 -*-

import re


def expression_to_list(expression):
    """
    讲字符串表达式转化为按顺序构成的列表,方便以后用堆栈实现四则运算
    感觉算法写的太烂了...但是也不知道有什么好方法可以快速的实现
    :param expression:
    :return sequence: 一个列表
    """
    expression = re.sub(r'\s*', '', expression)
    expression = expression.replace('+-', '-')
    expression = expression.replace('--', '+')
    symbols = '+-*/()'
    sequence = []
    number = ''

    # 将数字和运算符分开
    for c in expression:
        if c in symbols:
            if number:
                sequence.append(number)
            sequence.append(c)
            number = ''
        else:
            number += c
    if number:
        sequence.append(number)

    # 处理开头的负号,将负号与数字连为一体
    if sequence[0] == '-' and sequence[1] not in symbols:
        head = sequence.pop(0) + sequence.pop(0)
        sequence.insert(0, head)
    # 处理中间的符号,将负号与数字连为一体
    origin = sequence[:]
    sequence = []
    i = 0
    while i < len(origin):
        if origin[i] in '(*/' and origin[i + 1] == '-':
            sequence.append(origin[i])
            sequence.append(origin[i + 1] + origin[i + 2])
            i += 3
        else:
            sequence.append(origin[i])
            i += 1
    return sequence


def transform_suffix(expression):
    """
    将输入的表达式转换为后缀表达式
    :param expression:
    :return suffix: 返回后缀表达式,这种表达式没有括号,而且非常容易做下一步计算处理
    """
    sequence = expression_to_list(expression)
    suffix = []
    stack = []
    proirity_dict = {'*': 1, '/': 1, '+': 0, '-': 0, '(': 2, ')': 2}

    for c in sequence:
        if c not in proirity_dict:  # 如果c是数字,放入后缀表达式列表
            suffix.append(c)
        elif c != ')':

            while stack:
                top = stack[-1]
                if top == '(':
                    break
                if proirity_dict[top] >= proirity_dict[c]:
                    suffix.append(top)
                    del stack[-1]
                else:
                    break
            stack.append(c)
        else:  # c是')'
            top = stack[-1]
            while top != '(':
                suffix.append(top)
                del stack[-1]
                top = stack[-1]
            del stack[-1]
    stack.reverse()
    suffix.extend(stack)
    return suffix


def calculator(expression):
    """
    计算出表达式的值
    :param expression: 正确的计算表达式
    :return float: 表达式的值
    """
    suffix = transform_suffix(expression)
    operators = '+-*/'
    stack = []

    def add(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    func_dict = {'+': add, '-': minus, '*': mul, '/': div,}

    for c in suffix:
        if c not in operators:
            stack.append(float(c))
        else:
            y = stack.pop()
            x = stack.pop()
            z = func_dict[c](x, y)
            stack.append(z)
    return stack.pop()


if __name__ == '__main__':
    # expression = "(5+6000000)*10/(-1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) )"
    # expression = '1+2+3+((1+3+5)+(2+4+6)+(8+9+10)-(10-9-8)-(2+4+(1--9+9)*(10+-1)/(-1+12--2)))*12/3*-1/-2--1-3-2-1'
    # expression = '1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 + ((5+6000000)*10/(-1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) ) *1+2+3+((1+3+5)+(2+4+6)+(8+9+10)-(10-9-8)-(2+4+(1--9+9)*(10+-1)/(-1+12--2)))*12/3*-1/-2--1-3-2-1) )) - (-4*3)/ (16-3*2) )'
    expression = input('请输入算式:')
    # print(expression_to_list(expression))
    print('我的计算器的计算结果:')
    print(calculator(expression))
    print('eval的计算结果:')
    print(eval(expression))
