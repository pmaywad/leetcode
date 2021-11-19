"""
124. Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.globalmax = float("-inf")
        self.maxPathSumUtil(root)
        return self.globalmax
        
        
    def maxPathSumUtil(self, root):
        if not root:
            return 0

        
        pathSumL = max(0, self.maxPathSumUtil(root.left))
        pathSumR = max(0, self.maxPathSumUtil(root.right))
        pathSumRoot = root.val + pathSumL + pathSumR
        
        self.globalmax = max(pathSumRoot, self.globalmax)
        
        return max(pathSumL, pathSumR) + root.val
