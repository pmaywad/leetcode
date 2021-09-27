"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)- 1
        
        while l <= r:
            mid = l + (r-l)/2
            print(mid)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid -1
            else:
                l = mid + 1
        if target < nums[mid]:
            return mid
        else:
            return mid+1
