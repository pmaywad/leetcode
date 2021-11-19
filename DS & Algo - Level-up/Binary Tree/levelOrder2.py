"""
107. Binary Tree Level Order Traversal II
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        res = []
        queue.append(root)
        queue.append(None)
        level = []
        
        while queue:
            node = queue.pop(0)
            if node == None:
                res.append(level)
                level = []
                if queue:
                    queue.append(None)
            else:
            
                level.append(node.val)
    
                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
                    
        return res[:: -1]
        
