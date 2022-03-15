"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1

        if n <= 1:
            return head

        net_k = k % n
        net_k = n - net_k  # 3

        if net_k % n == 0:
            return head

        i = 0
        cur = head
        tmp = None
        while cur:
            if i == net_k - 1:
                tmp = cur.next  # 4
                cur.next = None  # 3.next = None
            elif i == net_k:
                new_head = cur
                tmp = None
            if i == n - 1:
                cur.next = head
            if tmp:
                cur = tmp
            else:
                cur = cur.next
            i += 1
        return new_head

"""
Runtime: 16 ms, faster than 98.88% of Python online submissions for Rotate List.
Memory Usage: 13.7 MB, less than 9.62% of Python online submissions for Rotate List.
"""