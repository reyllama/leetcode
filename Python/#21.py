"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        s = []
        while l1:
            s.append(l1.val)
            l1=l1.next
        while l2:
            s.append(l2.val)
            l2=l2.next
        s = sorted(s)
        for v in s:
            cur.next = ListNode(v)
            cur=cur.next
        return dummy.next

"""
Runtime: 40 ms, faster than 24.86% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.9 MB, less than 99.17% of Python3 online submissions for Merge Two Sorted Lists.
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next=ListNode(l2.val)
                cur=cur.next
                l2=l2.next
            else:
                cur.next=ListNode(l1.val)
                cur=cur.next
                l1=l1.next
        while l1:
            cur.next=ListNode(l1.val)
            cur=cur.next
            l1=l1.next
        while l2:
            cur.next=ListNode(l2.val)
            cur=cur.next
            l2=l2.next
        return dummy.next

"""
Runtime: 32 ms, faster than 86.27% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.9 MB, less than 99.17% of Python3 online submissions for Merge Two Sorted Lists.
"""
