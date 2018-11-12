#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    deque.py
# @Author:      Yalu
# @Time:        11/11/2018 7:30 PM
import unittest


class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class TestDeque(unittest.TestCase):
    def test(self):
        d = Deque()
        self.assertTrue(d.is_empty())
        d.add_rear(4)
        d.add_rear('dog')
        d.add_front('cat')
        d.add_front(True)
        self.assertEqual(d.size(), 4)
        self.assertFalse(d.is_empty())
        d.add_rear(8.4)
        self.assertEqual(d.remove_rear(), 8.4)
        self.assertEqual(d.remove_front(), True)

if __name__ == '__main__':
    unittest.main()