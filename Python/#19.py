"""
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        vals = []
        cur = ans = ListNode(0)
        while head:
            vals.append(head.val)
            head = head.next
        del vals[len(vals)-n]
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return ans.next

"""
Runtime: 28 ms, faster than 84.52% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.9 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.
"""
