class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        req = {}
        for i in range(len(nums)):
            if target-nums[i] in req:
                return [i, req[target-nums[i]]]
            else:
                req[nums[i]] = i
