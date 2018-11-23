#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    LinkedList.py
# @Author:      Yalu
# @Time:        16/11/2018 2:55 PM


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        current = self
        while index > 0 and current is not None:
            current = current.next
            index -= 1
        if current is not None and current.val is not None and index == 0:
            return current.val
        else:
            return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.val is None:
            self.val = val
        else:
            temp = MyLinkedList()
            temp.val = self.val
            temp.next = self.next
            self.val = val
            self.next = temp


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        current = self
        while current.next is not None:
            current = current.next
        node = MyLinkedList()
        node.addAtHead(val)
        current.next = node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        current = self
        while current.next is not None and index > 0:
            current = current.next
            index -= 1
        if current.val is not None and current.next is None and index == 1:
            current.next = MyLinkedList()
            current.next.val = val
        elif index == 0:
            temp = MyLinkedList()
            temp.val = current.val
            temp.next = current.next
            current.val = val
            current.next = temp

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        previous = None
        current = self
        while current.next is not None and index > 0:
            previous = current
            current = current.next
            index -= 1
        if index == 0:
            previous.next = current.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(0)
obj.addAtIndex(1,9)
obj.addAtIndex(1,5)
obj.addAtTail(7)
obj.addAtHead(1)
obj.addAtIndex(5,8)
obj.addAtIndex(5,2)
obj.addAtIndex(3,0)
obj.addAtTail(1)
obj.addAtTail(0)
obj.deleteAtIndex(6)
obj.deleteAtIndex(9)
print(obj.get(0))
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
print(obj.get(5))
print(obj.get(6))
print(obj.get(7))
print(obj.get(8))
print(obj.get(9))
print(obj.get(10))
