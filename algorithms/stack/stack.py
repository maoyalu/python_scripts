#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    stack.py
# @Author:      Yalu
# @Time:        10/11/2018 9:52 PM
import unittest


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return None if self.is_empty() else self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class TestStack(unittest.TestCase):
    def test(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        self.assertIsNone(s.peek())
        s.push(4)
        s.push('dog')
        self.assertEqual(s.peek(), 'dog')
        s.push(True)
        self.assertEqual(s.size(), 3)
        self.assertFalse(s.is_empty())
        s.push(8.4)
        self.assertEqual(s.pop(), 8.4)
        self.assertTrue(s.pop())
        self.assertEqual(s.size(), 2)


if __name__ == '__main__':
    unittest.main()