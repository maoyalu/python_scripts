#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    insertion.py
# @Author:      Yalu
# @Time:        12/11/2018 8:26 AM
import unittest


def insertion_sort(alist):
    for i in range(1, len(alist)):
        current = alist[i]
        pos = i
        while pos > 0 and alist[pos-1] > current:
            alist[pos] = alist[pos-1]
            pos -= 1
        alist[pos] = current


class TestThis(unittest.TestCase):
    def test(self):
        alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        insertion_sort(alist)
        self.assertEqual(alist, [17, 20, 26, 31, 44, 54, 55, 77, 93])


if __name__ == '__main__':
    unittest.main()