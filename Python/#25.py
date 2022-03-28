"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k==1:
            return head
        dummy = ListNode(val=0, next=head)
        cur = dummy
        
        def next_k(cur, k):
            i=0
            tmp = cur
            nodes = []
            while i<k and tmp.next:
                nodes.append(tmp.next)
                i += 1
                tmp = tmp.next
            return nodes
        
        while cur and cur.next:
            next_nodes = next_k(cur, k)
            q = next_nodes[-1].next
            if len(next_nodes)==k:
                next_nodes = next_nodes[::-1]
            for node in next_nodes:
                cur.next = node
                cur = node
            cur.next = q
        
        return dummy.next

"""
Runtime: 54 ms, faster than 44.18% of Python online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.3 MB, less than 19.51% of Python online submissions for Reverse Nodes in k-Group.
"""
