"""
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        vals = [head.val]
        cur = head
        out = 0

        while cur.next:
            cur = cur.next
            vals.append(cur.val)

        n = len(vals)

        for i, v in enumerate(vals):
            out += 2**(n-i-1) * v

        return out

"""
Runtime: 24 ms, faster than 96.61% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 14.4 MB, less than 8.12% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
"""
