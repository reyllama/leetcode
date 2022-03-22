"""
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""


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
        if not head:
            return None

        from collections import defaultdict

        cur = head
        vals = []
        prev = -101
        is_dup = defaultdict(bool)

        while cur:

            if cur.val == prev:
                is_dup[cur.val] = True
            else:
                vals.append(cur.val)
            prev = cur.val
            cur = cur.next

        distinct_vals = []
        for val in vals:
            if not is_dup[val]:
                distinct_vals.append(val)
        if not distinct_vals:
            return None
        distinct_vals = sorted(distinct_vals, reverse=True)

        val = distinct_vals.pop()
        newhead = ListNode(val)
        cur = newhead
        while distinct_vals:
            val = distinct_vals.pop()
            cur.next = ListNode(val)
            cur = cur.next

        return newhead

"""
Runtime: 32 ms, faster than 76.71% of Python online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 13.6 MB, less than 13.48% of Python online submissions for Remove Duplicates from Sorted List II.
"""