#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    bubble.py
# @Author:      Yalu
# @Time:        12/11/2018 8:08 AM
import unittest


def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


def bubble_sort_short(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum -= 1


class TestThis(unittest.TestCase):
    def test(self):
        alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        bubble_sort(alist)
        self.assertEqual(alist, [17, 20, 26, 31, 44, 54, 55, 77, 93])

    def test2(self):
        alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        bubble_sort_short(alist)
        self.assertEqual(alist, [17, 20, 26, 31, 44, 54, 55, 77, 93])


if __name__ == '__main__':
    unittest.main()