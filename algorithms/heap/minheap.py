#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    minheap.py
# @Author:      Yalu
# @Time:        12/11/2018 9:12 AM
import unittest


class MinHeap:
    def __init__(self):
        self.items = [0]
        self.size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.items[i] < self.items[i//2]:
                self.items[i], self.items[i//2] = self.items[i//2], self.items[i]
            i //= 2

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.perc_up(self.size)

    def perc_down(self, i):
        while i * 2 <= self.size:
            mc = self.min_child(i)
            if self.items[i] > self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 <= self.size and self.items[i*2] > self.items[i*2+1]:
            return i * 2 + 1
        else:
            return i * 2

    def del_min(self):
        item = self.items[1]
        self.items[1] = self.items[self.size]
        self.size -= 1
        self.items.pop()
        self.perc_down(1)
        return item

    def build_heap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.items = [0] + alist
        while i > 0:
            self.perc_down(i)
            i -= 1


class TestMinHeap(unittest.TestCase):
    def test(self):
        heap = MinHeap()
        heap.build_heap([9, 5, 6, 2, 3])
        self.assertEqual(heap.del_min(), 2)
        self.assertEqual(heap.del_min(), 3)
        self.assertEqual(heap.del_min(), 5)
        self.assertEqual(heap.del_min(), 6)
        self.assertEqual(heap.del_min(), 9)


if __name__ == '__main__':
    unittest.main()