#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    binary.py
# @Author:      Yalu
# @Time:        11/11/2018 10:51 PM
import unittest


def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if alist[middle] == item:
            found = True
        elif alist[middle] > item:
            last = middle - 1
        else:
            first = middle + 1
    return found


def binary_search_recursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        middle = len(alist) // 2
        if alist[middle] == item:
            return True
        elif alist[middle] > item:
            return binary_search_recursive(alist[:middle], item)
        else:
            return binary_search_recursive(alist[middle+1:], item)


class TestThis(unittest.TestCase):
    def test(self):
        l1 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        self.assertFalse(binary_search(l1, 3))
        self.assertTrue(binary_search(l1, 13))

    def test2(self):
        l1 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        self.assertFalse(binary_search(l1, 3))
        self.assertTrue(binary_search(l1, 13))
        self.assertTrue(binary_search(l1, 42))
        self.assertTrue(binary_search(l1, 0))



if __name__ == '__main__':
    unittest.main()