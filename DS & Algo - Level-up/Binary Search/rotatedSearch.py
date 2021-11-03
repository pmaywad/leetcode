'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)/2
            
            if nums[mid] == target:
                return mid
            
            elif nums[start]<=nums[mid]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[mid] < nums[end]:
                    if nums[mid] <= target and target <= nums[end]:
                        start = mid+1
                    else:
                        end = mid-1
                        
        return -1
        
