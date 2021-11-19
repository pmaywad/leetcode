"""
103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
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
        Odd = True
        prev_node = None
        level = []
        while queue:
            #print(level)
            node = queue.pop(0)
            if node == None:
                if Odd:
                    res.append(level)
                else:
                    res.append(level[::-1])
                    
                level = []
                if queue:
                    queue.append(None)
                Odd = Odd ^ True
            else:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return res
