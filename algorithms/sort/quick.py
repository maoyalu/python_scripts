#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    quick.py
# @Author:      Yalu
# @Time:        12/11/2018 8:37 AM
import unittest


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)
        quick_sort_helper(alist, first, split_point-1)
        quick_sort_helper(alist, split_point+1, last)


def partition(alist, first, last):
    pivot = alist[first]

    left = first + 1
    right = last

    done = False
    while not done:
        while left <= right and alist[left] <= pivot:
            left += 1
        while right >= left and alist[right] >= pivot:
            right -= 1
        if left > right:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]
    alist[first], alist[right] = alist[right], alist[first]

    return right


class TestThis(unittest.TestCase):
    def test(self):
        alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        quick_sort(alist)
        self.assertEqual(alist, [17, 20, 26, 31, 44, 54, 55, 77, 93])


if __name__ == '__main__':
    unittest.main()