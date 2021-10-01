"""
213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob_linear(self, nums):
        memo = [0]*len(nums)
        if len(nums) == 1:
            return nums[0]
        memo[0] = nums[0]
        memo[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            memo[i] = max(memo[i-1], memo[i-2]+nums[i])

        return memo[-1]    
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))
