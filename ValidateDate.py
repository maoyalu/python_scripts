#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    ValidateDate.py
# @Author:      Yalu
# @Time:        2/10/2018 8:11 PM
"""
Validate a date formatted as 'DD/MM/YYYY'
Return True if this date exist
Return False otherwise
"""
import datetime
import re


# use strptime() method to validate
def validate_date_dt(date_str):
    try:
        datetime.datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False


# check if it is a leap year, look up and adjust the maximum number of days
def validate_date_re(date_str):
    if re.match('\d{2}/\d{2}/\d{4}', date_str) is not None:
        day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date = date_str.split('/')
        year = int(date[2])
        last_day = day[int(date[1]) - 1]
        if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) and date[1] == '02':
            last_day += 1
        return 0 <= int(date[0]) <= last_day and 1 <= int(date[1]) <= 12
    else:
        return False
