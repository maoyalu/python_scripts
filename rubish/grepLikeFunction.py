#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    grepLikeFunction.py
# @Author:      Yalu
# @Time:        2/12/2018 10:48 PM


def grepLikeFunction(input):
    input = input.split('\n')
    word = input[0]
    count = 1

    for line in input:
        if word in line:
            print(str(count) + ':' + line.replace(word, '{' + word + '}'))
        count += 1




grepLikeFunction('a\nWhen You fall in Love with someone fall')