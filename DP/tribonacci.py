"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution(object):
    def tribonacci(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """
        if memo.get(n):
            return memo[n]
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        memo[n] = self.tribonacci(n-1, memo) + self.tribonacci(n-2, memo) + self.tribonacci(n-3, memo)
        return memo[n]
