"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        cur = head
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        val = vals.pop()
        head = ListNode(val=val)
        cur = head
        while vals:
            val = vals.pop()
            cur.next = ListNode(val=val)
            cur = cur.next
        return head

"""
Runtime: 24 ms, faster than 76.94% of Python online submissions for Reverse Linked List.
Memory Usage: 17.2 MB, less than 16.66% of Python online submissions for Reverse Linked List.
"""