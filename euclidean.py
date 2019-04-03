#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    euclidean.py
# @Author:      Yalu
# @Time:        3/04/2019 6:07 PM


def euclidean(a, b):
    if a < b:
        return euclidean(b, a)
    elif b == 0:
        return a
    else:
        return euclidean(b, a % b)


def euclidean_extended(a, b):
    if a < b:
        return euclidean_extended(b, a)
    elif b == 0:
        return a, 1, 0
    else:
        # a = 1 * a + 0 * b
        # b = 0 * a + 1 * b
        x_pre, y_pre = 1, 0
        x, y = 0, 1

        while b > 0:
            q = a // b
            r = a - q * b
            x_temp = x_pre - q * x
            y_temp = y_pre - q * y

            a = b
            b = r
            x_pre = x
            x = x_temp
            y_pre = y
            y = y_temp

        return a, x_pre, y_pre


# The result should be (1, -111, 355)
print(euclidean_extended(1759, 550))