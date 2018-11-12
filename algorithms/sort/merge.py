#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    merge.py
# @Author:      Yalu
# @Time:        12/11/2018 8:32 AM
import unittest


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1


def merge_sort_index(alist, low=0, high=None):
    if high is None:
        high = len(alist) - 1
    if high > low:
        mid = (high + low) // 2
        merge_sort_index(alist, low, mid)
        merge_sort_index(alist, mid+1, high)

        i = low
        j = mid + 1
        temp = []
        while i < mid + 1 and j < high + 1:
            if alist[i] < alist[j]:
                temp.append(alist[i])
                i += 1
            else:
                temp.append(alist[j])
                j += 1
        while i < mid + 1:
            temp.append(alist[i])
            i += 1
        while j < high + 1:
            temp.append(alist[j])
            j += 1
        alist[low: high+1] = temp


class TestThis(unittest.TestCase):
    def test(self):
        alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        merge_sort(alist)
        self.assertEqual(alist, [17, 20, 26, 31, 44, 54, 55, 77, 93])

    def test2(self):
        alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        merge_sort_index(alist)
        self.assertEqual(alist, [17, 20, 26, 31, 44, 54, 55, 77, 93])


if __name__ == '__main__':
    unittest.main()