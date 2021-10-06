"""
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0]*len(cost)
        if len(cost) == 1:
            return cost[0]
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            
        return min(dp[len(cost)-1], dp[len(cost)-2])