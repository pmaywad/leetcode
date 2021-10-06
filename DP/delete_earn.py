'''
740. Delete and Earn

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.
'''

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Reduced to house robber
        
        if  not nums:
            return 0

        freq = [0] * (max(nums)+1)
        for n in nums:
            freq[n] += n

        dp = [0] * len(freq)
        dp[1] = freq[1]
        for i in range(2, len(freq)):
            dp[i] = max(freq[i] + dp[i-2], dp[i-1])

        return dp[len(freq)-1]
