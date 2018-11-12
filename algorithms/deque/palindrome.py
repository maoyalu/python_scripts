#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    palindrome.py
# @Author:      Yalu
# @Time:        11/11/2018 7:39 PM
import unittest
from .deque import Deque


def palindrome_checker(string):
    d = Deque()
    for char in string:
        d.add_front(char)
    valid = True
    while d.size() > 1 and valid:
        if d.remove_rear() != d.remove_front():
            valid = False
    return valid

class TestThis(unittest.TestCase):
    def test(self):
        self.assertFalse(palindrome_checker('lsdkjfskf'))
        self.assertTrue(palindrome_checker('radar'))


if __name__ == '__main__':
    unittest.main()