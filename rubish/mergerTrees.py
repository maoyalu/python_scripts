#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    mergerTrees.py
# @Author:      Yalu
# @Time:        16/11/2018 4:17 PM

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mergeTrees(t1, t2):
    t1.val += t2.val

    if t1.left is not None and t2.left is not None:
        mergeTrees(t1.left, t2.left)
    elif t1.left is None and t2.left is not None:
        t1.left = t2.left

    if t1.right is not None and t2.right is not None:
        mergeTrees(t1.right, t2.right)
    elif t1.right is None and t2.right is not None:
        t1.right = t2.right

    return t1


t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

t2= TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(7)

t3 = mergeTrees(t1, t2)

print(t3.val)
print(t3.left.val)
print(t3.right.val)
print(t3.left.left.val)
print(t3.left.right.val)
print(t3.right.right.val)