#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    unordered_list.py
# @Author:      Yalu
# @Time:        11/11/2018 7:53 PM
import unittest
from .node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next

    def append(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            next_pos = 1
            current = self.head
            while next_pos < pos:
                current = current.next
                next_pos += 1
            temp = Node(item)
            temp.next = current.next
            current.next = temp

    def index(self, item):
        pos = 0
        current = self.head
        while current.data != item:
            current = current.next
            pos += 1
        return pos if current is not None else None

    def pop(self, pos=None):
        if pos is None:
            pos = self.size() - 1
        item = None
        if pos == 0:
            item = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            next_pos = 1
            while next_pos < pos:
                current = current.next
                next_pos += 1
            item = current.next.data
            current.next = current.next.next
        return item


class TestUnorderedList(unittest.TestCase):
    def setUp(self):
        self.l1 = UnorderedList()
        self.l2 = UnorderedList()
        self.l2.add(1)
        self.l2.add(3)
        self.l2.add(2)

    def test_is_empty(self):
        self.assertTrue(self.l1.is_empty())
        self.l1.add('a')
        self.assertFalse(self.l1.is_empty())

    def test_add(self):
        self.l1.add('a')
        self.assertTrue(self.l1.search('a'))
        self.l1.add('b')
        self.assertTrue(self.l1.search('a'))
        self.assertTrue(self.l1.search('b'))
        self.l1.add('a')
        self.assertTrue(self.l1.search('a'))
        self.l1.remove('a')
        self.assertTrue(self.l1.search('a'))

    def test_size(self):
        self.assertEqual(self.l1.size(), 0)
        self.assertEqual(self.l2.size(), 3)

    def test_search(self):
        self.assertFalse(self.l1.search('a'))
        self.assertFalse(self.l2.search('a'))
        self.assertTrue(self.l2.search(1))
        self.assertTrue(self.l2.search(2))
        self.assertTrue(self.l2.search(3))

    def test_remove(self):
        self.l2.remove(1)
        self.assertFalse(self.l2.search(1))
        self.assertTrue(self.l2.search(2))
        self.assertTrue(self.l2.search(3))
        self.l2.add(2)
        self.l2.remove(2)
        self.assertTrue(self.l2.search(2))

    def test_append(self):
        self.l1.append('a')
        self.assertTrue(self.l1.search('a'))
        self.l1.remove('a')
        self.assertFalse(self.l1.search('a'))
        self.l2.append(5)
        self.assertEqual(self.l2.pop(), 5)

    def test_index(self):
        self.assertEqual(self.l2.index(1), 2)
        self.assertEqual(self.l2.index(3), 1)
        self.assertEqual(self.l2.index(2), 0)

    def test_insert(self):
        self.l1.insert(0, 'a')
        self.assertEqual(self.l1.index('a'), 0)
        self.l1.insert(0, 'b')
        self.assertEqual(self.l1.index('b'), 0)
        self.assertEqual(self.l1.index('a'), 1)
        self.l1.insert(1, 'c')
        self.assertEqual(self.l1.index('b'), 0)
        self.assertEqual(self.l1.index('c'), 1)
        self.assertEqual(self.l1.index('a'), 2)
        self.l1.insert(3, 'd')
        self.assertEqual(self.l1.index('d'), 3)

    def test_pop(self):
        self.assertEqual(self.l2.pop(), 1)
        self.assertEqual(self.l2.size(), 2)
        self.assertEqual(self.l2.pop(), 3)
        self.assertEqual(self.l2.size(), 1)
        self.l2.append(4)
        self.assertEqual(self.l2.pop(), 4)
        self.assertEqual(self.l2.size(), 1)

    def test_pop_with_arg(self):
        self.assertEqual(self.l2.pop(1), 3)
        self.assertEqual(self.l2.size(), 2)


if __name__ == '__main__':
    unittest.main()