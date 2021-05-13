"""
1669. Merge In Between Linked Lists

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure incidate the result:
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        idx = 1
        cur1 = list1
        cur2 = list1

        while True:
            if idx == a:
                tmp1 = cur1
            if idx == b:
                tmp2 = cur1.next.next
                break
            idx += 1
            cur1 = cur1.next
        tmp1.next = list2 # connect tmp1 to beginning of list2
        while list2.next:
            list2 = list2.next
        list2.next = tmp2 # connect end of list2 to tmp2

        idx = 1
        list1.next = cur2.next # bind list1 to cur2
        while True:
            if idx == a:
                cur2.next = tmp1.next # Connect cur2 to tmp1
                break
            idx += 1
            cur2 = cur2.next  
        return list1            

"""
Runtime: 500 ms, faster than 52.31% of Python online submissions for Merge In Between Linked Lists.
Memory Usage: 24.6 MB, less than 28.70% of Python online submissions for Merge In Between Linked Lists.
"""
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        c=0
        head=check=list1
        while list1:
            c+=1
            if c>=a:
                check=check.next
            else:
                list1=list1.next
                check=check.next
            if c==b:
                check=check.next
                break
        list1.next=list2
        while list2.next:
            list2=list2.next
        list2.next=check
        return head
