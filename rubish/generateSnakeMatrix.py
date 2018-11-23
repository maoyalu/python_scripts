#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    generateSnakeMatrix.py
# @Author:      Yalu
# @Time:        23/11/2018 11:36 PM


def generator(row, column, turn):
    print('Generated matrix:')
    matrix = [[] for _ in range(row)]
    num = 1
    num_list = 0
    while num <= row * column:
        if turn:
            for i in range(num_list, -1, -1):
                if len(matrix[i]) < column:
                    matrix[i].append(num)
                    num += 1
        else:
            for i in range(num_list+1):
                if len(matrix[i]) < column:
                    matrix[i].append(num)
                    num += 1
        if num_list + 1 < row:
            num_list += 1
        turn = not turn

    for x in range(len(matrix)):
        for j in range(len(matrix[x])):
            print(matrix[x][j], end='\t')
        print()
    print()


generator(6, 7, True)

generator(6, 7, False)
