'''
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hash_map = {}
        
        temp = head
        prev = None
        while temp:
            if not temp.val in hash_map:
                hash_map[temp.val] = 1
                prev = temp
            else:
                prev.next = temp.next
                
            temp = temp.next
            
        return head
