#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    GuessNumber.py
# @Author:      Yalu
# @Time:        2/10/2018 8:32 PM


import random


def guess_number():
    x = random.randint(0, 100)
    count = 1
    minnum = 0
    maxnum = 100
    while True:
        try:
            y = int(input('Input guess: '))
            if x == y:
                break
            elif y < x < y + 10:
                print("That's too low.")
                minnum = max(y + 1, minnum)
                maxnum = min(y + 9, maxnum)
            elif x >= y + 10:
                print("That's way too low!")
                minnum = max(y + 10, minnum)
            elif y - 10 < x < y:
                print("That's too high.")
                maxnum = min(y - 1, maxnum)
                minnum = max(y - 9, minnum)
            else:
                print("That's way too high!")
                maxnum = min(y - 10, maxnum)
            count += 1
        except ValueError:
            print('Invalid input')
        print('Guess in', end=' ')
        for i in range(minnum, maxnum + 1):
            print(i, end=' ')
        print()
    print('Good guess! It only took you {} tries'.format(count))


if __name__ == '__main__':
    guess_number()
    input('Press <ENTER> to exit')