#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    anagram.py
# @Author:      Yalu
# @Time:        11/11/2018 11:37 AM
import unittest


def is_anagram(s1, s2):
    """
    First check if these two strings have the same length, if no they are not anagrams.
    Then convert string1 to a list, compare each character of string2 with the list. If the character is found in the
    list, change it to None and move to the next character. Otherwise, it is not a anagram.
    The complexity is O(n^2).
    """
    if len(s1) != len(s2):
        return False
    else:
        s1 = list(s1)
        match = True
        pos2 = 0
        while pos2 < len(s2) and match:
            pos1 = 0
            found = False
            while pos1 < len(s1) and not found:
                if s1[pos1] == s2[pos2]:
                    s1[pos1] = None
                    found = True
                else:
                    pos1 += 1
            pos2 += 1
            if not found:
                match = False
        return match


def is_anagram_sort(s1, s2):
    """
    First check if these two strings have the same length, if no they are not anagrams.
    Then convert both strings to lists, and sort the lists.
    Check if their characters match with each other.
    The complexity is O(nlogn) or O(n^2), depending on the sorting.
    """
    if len(s1) != len(s2):
        return False
    else:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        pos = 0
        match = True
        while pos < len(s1) and match:
            if s1[pos] == s2[pos]:
                pos += 1
            else:
                match = False
    return match


def is_anagram_count(s1, s2):
    """
    Count the occurrence of the characters and compare the count.
    The complexity is O(1).
    """
    count1 = [0] * 26
    count2 = [0] * 26
    for i in range(len(s1)):
        count1[ord(s1[i]) - ord('a')] += 1
    for i in range(len(s2)):
        count2[ord(s2[i]) - ord('a')] += 1
    pos = 0
    match = True
    while pos < 26 and match:
        if count1[pos] == count2[pos]:
            pos += 1
        else:
            match = False
    return match


class TestThis(unittest.TestCase):
    def test1(self):
        self.assertTrue(is_anagram('', ''))
        self.assertTrue(is_anagram('abcd', 'dcba'))
        self.assertFalse(is_anagram('abcd', 'dcbad'))

    def test2(self):
        self.assertTrue(is_anagram_sort('', ''))
        self.assertTrue(is_anagram_sort('abcd', 'dcba'))
        self.assertFalse(is_anagram_sort('abcd', 'dcbad'))

    def test3(self):
        self.assertTrue(is_anagram_count('', ''))
        self.assertTrue(is_anagram_count('abcd', 'dcba'))
        self.assertFalse(is_anagram_count('abcd', 'dcbad'))


if __name__ == '__main__':
    unittest.main()