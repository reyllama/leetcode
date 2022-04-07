"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        curs = [cur for cur in lists]
        
        while any(curs):
            curMin = 1e4+1
            curMin_idx = -1
            for i, node in enumerate(curs):
                if node and node.val < curMin:
                    curMin = node.val
                    curMin_idx = i
            if not head:
                head = ListNode(curMin)
                c = head
            else:
                c.next = ListNode(curMin)
                c = c.next
            curs[curMin_idx] = curs[curMin_idx].next
        return head

"""
Runtime: 6424 ms, faster than 5.01% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 22.3 MB, less than 32.07% of Python online submissions for Merge k Sorted Lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        mid = len(lists)//2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
        
    def merge(self, l, r):
        p = dummy = ListNode()
        while l and r:
            if l.val > r.val:
                p.next = r
                r = r.next
            else:
                p.next = l
                l = l.next
            p = p.next
        p.next = l or r
        return dummy.next

"""
Runtime: 101 ms, faster than 83.69% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 19.4 MB, less than 84.36% of Python online submissions for Merge k Sorted Lists.
"""
