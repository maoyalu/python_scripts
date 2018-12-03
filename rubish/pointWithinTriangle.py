#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    pointWithinTriangle.py
# @Author:      Yalu
# @Time:        2/12/2018 10:20 PM
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def pointIsWithin(A, B, C, P):
    MA = Point(P.x-A.x, P.y-A.y)
    MB = Point(P.x-B.x, P.y-B.y)
    MC = Point(P.x-C.x, P.y-B.y)

    a = MA.x * MB.y - MA.y * MB.x
    b = MB.x * MC.y - MB.y * MC.x
    c = MC.x * MA.y - MC.y * MA.x

    return (a <= 0 and b <= 0 and c <= 0) or (a >= 0 and b >= 0 and c >= 0)


if __name__ == '__main__':
    count = int(sys.stdin.readline().strip())
    result = ''
    for i in range(count):
        data = sys.stdin.readline().strip().split(' ')
        A = Point(float(data[0]), float(data[1]))
        B = Point(float(data[2]), float(data[3]))
        C = Point(float(data[4]), float(data[5]))
        P = Point(float(data[6]), float(data[7]))
        if pointIsWithin(A, B, C, P):
            result += '1'
        else:
            result += '0'
        count -= 1
        if count != 0:
            result += '\n'
    print(result, end='')


outputResult('2\n-1.0 1.0 -3.0 4.0 -4.0 1.0 -2.0 2.0\n1 1 3 4 4 1 0 0')
