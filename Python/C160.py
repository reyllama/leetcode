"""
160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

<pic>

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A, B = headA, headB
        while A!=B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

"""
Runtime: 196 ms, faster than 65.07% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 43.4 MB, less than 36.42% of Python online submissions for Intersection of Two Linked Lists.
"""