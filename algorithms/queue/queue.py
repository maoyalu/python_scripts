#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    queue.py
# @Author:      Yalu
# @Time:        11/11/2018 7:18 PM
import unittest


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class TestStack(unittest.TestCase):
    def test(self):
        q = Queue()
        q.enqueue(4)
        q.enqueue('dog')
        q.enqueue(True)
        self.assertEqual(q.size(), 3)
        self.assertFalse(q.is_empty())
        q.enqueue(8.4)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 'dog')
        self.assertEqual(q.size(), 2)


if __name__ == '__main__':
    unittest.main()
