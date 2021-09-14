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
        temp = head
        while temp:
            temp = temp.next
            length += 1

        mid = length//2
        temp = head
        while mid >= 1:
            temp = temp.next
            mid -= 1

        return temp
