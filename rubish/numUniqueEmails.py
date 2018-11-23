#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    numUniqueEmails.py
# @Author:      Yalu
# @Time:        16/11/2018 3:49 PM


def numUniqueEmails(emails):
    email_list = set()
    for email in emails:
        local, domain = email.split('@')
        if '+' in local:
            local = local[:local.index('+')]
        email_list.add(local.replace('.', '') + '@' + domain)
    return len(email_list)


numUniqueEmails(['y.a+.l.u@yalu.com', 'ya@ya.lu.com'])