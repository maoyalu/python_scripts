#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    postfix_expression.py
# @Author:      Yalu
# @Time:        11/11/2018 2:42 PM
from .stack import Stack
import unittest


def infix_to_postfix(infix_expr):
    precedence = {'(': 0,
                  ')': 0,
                  '+': 1,
                  '-': 1,
                  '*': 2,
                  '/': 2,
                  '**': 3}
    ops = Stack()
    postfix_list = []
    tokens = infix_expr.split()
    for token in tokens:
        if token == '(':
            ops.push(token)
        elif token == ')':
            top = ops.pop()
            while top != '(':
                postfix_list.append(top)
                top = ops.pop()
        elif token not in precedence.keys():
            postfix_list.append(token)
        else:
            while not ops.is_empty() and precedence[ops.peek()] >= precedence[token]:
                postfix_list.append(ops.pop())
            ops.push(token)
    while not ops.is_empty():
        postfix_list.append(ops.pop())
    return ' '.join(postfix_list)


def postfix_eval(postfix_expr):
    ops = Stack()
    tokens = postfix_expr.split()
    for token in tokens:
        if token in '**/+-':
            op2 = ops.pop()
            op1 = ops.pop()
            ops.push(calculate(token, op1, op2))
        else:
            ops.push(int(token))
    return ops.pop()


def calculate(token, op1, op2):
    if token == '*':
        return op1 * op2
    elif token == '/':
        return op1 / op2
    elif token == '+':
        return op1 + op2
    elif token == '-':
        return op1 - op2
    elif token == '**':
        return op1 ** op2


def infix_eval(infix_expr):
    return postfix_eval(infix_to_postfix(infix_expr))


class TestThis(unittest.TestCase):
    def test(self):
        self.assertEqual(infix_to_postfix("A * B + C * D"), 'A B * C D * +')
        self.assertEqual(infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )'), 'A B + C * D E - F G + * -')
        self.assertEqual(infix_to_postfix("( A + B ) * ( C + D )"), 'A B + C D + *')
        self.assertEqual(infix_to_postfix("( A + B ) * C"), 'A B + C *')
        self.assertEqual(infix_to_postfix("A + B * C"), 'A B C * +')
        self.assertEqual(infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )"), '10 3 5 * 16 4 - / +')
        self.assertEqual(infix_to_postfix("5 * 3 ** ( 4 - 2 )"), '5 3 4 2 - ** *')

    def test2(self):
        self.assertEqual(postfix_eval('7 8 + 3 2 + /'), 3)
        self.assertEqual(postfix_eval('5 3 4 2 - ** *'), 45)

    def test3(self):
        self.assertEqual(infix_eval('5 * 3 ** ( 4 - 2 )'), 45)


if __name__ == '__main__':
    unittest.main()
