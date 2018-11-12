#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    selection.py
# @Author:      Yalu
# @Time:        12/11/2018 8:19 AM
import unittest


def selection_sort(alist):
    for i in range(len(alist)-1, 0, -1):
        pos = 0
        for j in range(1, i+1):
            if alist[j] > alist[pos]:
                pos = j
        alist[i], alist[pos] = alist[pos], alist[i]


class TestThis(unittest.TestCase):
    def test(self):
        alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        selection_sort(alist)
        self.assertEqual(alist, [17, 20, 26, 31, 44, 54, 55, 77, 93])


if __name__ == '__main__':
    unittest.main()
