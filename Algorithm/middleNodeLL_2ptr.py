# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        slowptr = head
        fastptr = head
        while fastptr and fastptr.next:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
        
        return slowptr
            
