#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    FindThreeNumSumZero.py
# @Author:      Yalu
# @Time:        2/10/2018 8:28 PM
"""
Input a list of integers
Print all combinations of three numbers with a sum of 0
"""


def find_sum_zero(li):
    if li is None or len(li) < 3:
        return None
    else:
        current = 0
        for i in range(len(li) - 2):
            end = len(li) - 1
            head = current + 1
            while head != end:
                if li[current] + li[head] + li[end] > 0:
                    end -= 1
                elif li[current] + li[head] + li[end] < 0:
                    head += 1
                else:
                    print([li[current], li[head], li[end]])
                    break
            current += 1


find_sum_zero([-25, -10, -7, -3, 2, 4, 8, 10])