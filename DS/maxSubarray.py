"53. Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array."

from sys import maxint
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = -maxint-1
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_so_far:
                max_so_far = curr_sum
            
            if curr_sum < 0:
                curr_sum = 0
        
        return max_so_far
