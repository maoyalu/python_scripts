#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    twoSum.py
# @Author:      Yalu
# @Time:        16/11/2018 2:01 PM


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index = {}
    for i in range(len(nums)):
        index[nums[i]] = i
    nums.sort()
    size = len(nums)
    for i in range(size):
        j = i + 1
        while j < size and nums[i] + nums[j] <= target:
            if nums[i] + nums[j] == target:
                return[index[nums[i]], index[nums[j]]]
            j += 1


print(twoSum([2, 5, 7, 11, 15], 12))
print(twoSum([3, 2, 4], 6))
print(twoSum([0, 4, 3, 0], 0))
print(twoSum([-3,4,3,90], 0))