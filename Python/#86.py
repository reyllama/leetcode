"""
86. Partition List


Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        left, right = [], []
        cur = head
        while cur:
            if cur.val < x:
                left.append(cur.val)
            else:
                right.append(cur.val)
            cur = cur.next
        vals = left + right
        vals = vals[::-1]
        newhead = ListNode(vals.pop())
        cur = newhead
        while vals:
            tmp = vals.pop()
            cur.next = ListNode(tmp)
            cur = cur.next
        return newhead
"""
Runtime: 31 ms, faster than 50.57% of Python online submissions for Partition List.
Memory Usage: 13.5 MB, less than 35.37% of Python online submissions for Partition List.
"""