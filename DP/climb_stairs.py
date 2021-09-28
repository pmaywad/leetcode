"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution(object):
    def climbStairs(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """
        if memo.get(n):
            return memo[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n]
