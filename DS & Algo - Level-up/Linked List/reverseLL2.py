"""
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        if right == left:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for i in range(left-1):
            prev = prev.next
            
        current = prev.next
        nxt = current.next
        
        for i in range(right-left):
            temp = nxt.next
            nxt.next = current
            current = nxt
            nxt = temp
            
        prev.next.next = nxt
        prev.next = current
        
        return dummy.next
        
