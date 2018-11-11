#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    balance_symbol.py
# @Author:      Yalu
# @Time:        11/11/2018 12:48 PM
from .stack import Stack
import unittest


def balance_checker(symbols):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbols) and balanced:
        current = symbols[index]
        if current in '([{':
            s.push(current)
        else:
            if s.is_empty():
                balanced = False
            else:
                if '([{'.index(s.pop()) != ')]}'.index(current):
                    balanced = False
        index += 1
    return s.is_empty() and balanced


class TestThis(unittest.TestCase):
    def test(self):
        self.assertTrue(balance_checker('((()))'))
        self.assertFalse(balance_checker('(()'))
        self.assertFalse(balance_checker('[{()]'))
        self.assertTrue(balance_checker('{{([][])}()}'))


if __name__ == '__main__':
    unittest.main()

