"""
114. Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        if not root.right and not root.left:
            return root
        
        left = root.left
        right = root.right
        
        root.right = self.flatten(left)
        root.left = None
        temp = root
        while temp.right:
            temp = temp.right
        temp.right = self.flatten(right)
        
        return root
