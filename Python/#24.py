"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if (head is None) or (head.next is None):
            return head
        
        res = head.next # 2
        cur = res # 2
        tmp1 = cur.next # 3 (could be None)
        cur.next = head # 1
        cur = cur.next # 1
        cur.next = tmp1 # 3
        
        while True:
        
            if (tmp1 is None) or (tmp1.next is None):
                return res
        
            else:
                tmp2 = tmp1.next # 4
                cur.next = tmp2 # 4
                tmp1.next = tmp2.next # 5
                cur.next.next = tmp1 # 3
                tmp1 = tmp1.next # 5
                cur = cur.next.next # 3

"""
Runtime: 26 ms, faster than 49.55% of Python online submissions for Swap Nodes in Pairs.
Memory Usage: 13.5 MB, less than 31.71% of Python online submissions for Swap Nodes in Pairs.
"""