#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    longestIncreasePathInMatrix.py
# @Author:      Yalu
# @Time:        2/12/2018 10:57 PM
import sys


def compare(matrix, visited, length, row, column):
    horizontal = [-1, 1, 0, 0]
    vertical = [0, 0, -1, 1]
    m = len(matrix)
    n = len(matrix[0])
    if visited[row][column]:
        return length[row][column]
    length[row][column] = 1
    for i in range(4):
        x = row + horizontal[i]
        y = column + vertical[i]
        if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[row][column]:
            length[row][column] = max(length[row][column], compare(matrix, visited, length, x, y) + 1)
    visited[row][column] = True
    return length[row][column]


if __name__ == '__main__':
    m, n = sys.stdin.readline().strip()
    m = int(m)
    n = int(n)
    matrix = [[] for _ in range(m)]
    for i in range(m):
        matrix[i] = sys.stdin.readline().strip().split(',')
    visited = [[False for _ in range(n)] for _ in range(m)]
    length = [[0 for _ in range(n)] for _ in range(m)]
    result = 0
    for row in range(m):
        for column in range(n):
            result = max(result, compare(matrix, visited, length, row, column))

    print(result)


solution('3 3\n9,9,4\n6,6,8\n2,1,1')