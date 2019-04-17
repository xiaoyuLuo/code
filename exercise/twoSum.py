# !/usr/bin/env python
# -*- coding: utf-8 -*-#

"""
 Name:         twoNum
 Description:  给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
               你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
 Author:       xiaoyuLuo
 Date:         2019/4/17
"""


class Solution:
    def twoSum(self, nums, target):
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        return "no solution"

    def twoSumSecond(self, nums, target):
        nums_len = len(nums)
        for i in range(nums_len):
            try:
                index = nums.index(target - nums[i])
            except:
                # 没有找到
                index = -1

            if index != -1 and index != i:
                return [i, index]

        return "no solution"


if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.twoSum([3,2,4], 6))
