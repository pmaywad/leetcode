"""
116. Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        queue = []
        queue.append(root)
        queue.append(None)
        
        prevNode = None
        
        while queue:
            #print(queue)
            node = queue.pop(0)
            if node == None:
                if prevNode:
                    prevNode.next = None
                if queue:
                    queue.append(None)
            else:
                if prevNode:
                    prevNode.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            prevNode = node
                
        return root
