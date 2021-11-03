'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        first_idx = self.firstOccurrence(nums, target)
        last_idx = self.lastOccurrence(nums, target)
        
        return [first_idx, last_idx]
    
    
    def firstOccurrence(self, nums, target):
        
        ans = -1
        start = 0
        end = len(nums) - 1
        while start<=end:
            mid = (start+end)/2
            if nums[mid] == target:
                ans = mid
                end = mid-1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return ans
    
    def lastOccurrence(self, nums, target):
        
        ans = -1
        start = 0
        end = len(nums) - 1
        while start<=end:
            mid = (start+end)/2
            if nums[mid] == target:
                ans = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return ans
