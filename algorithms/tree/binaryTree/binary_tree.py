#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    binary_tree.py
# @Author:      Yalu
# @Time:        12/11/2018 8:59 AM
import unittest


class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, item):
        if self.left is None:
            self.left = BinaryTree(item)
        else:
            node = BinaryTree(item)
            node.left = self.left
            self.left = node

    def insert_right(self, item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            node = BinaryTree(item)
            node.right = self.right
            self.right = node


class TestBinaryTree(unittest.TestCase):
    def test(self):
        tree = BinaryTree('a')
        self.assertEqual(tree.key, 'a')
        self.assertEqual(tree.left, None)
        tree.insert_left('b')
        self.assertEqual(tree.left.key, 'b')
        tree.insert_right('c')
        self.assertEqual(tree.right.key, 'c')
        tree.insert_left('d')
        self.assertEqual(tree.left.key, 'd')
        self.assertEqual(tree.left.left.key, 'b')


if __name__ == '__main__':
    unittest.main()