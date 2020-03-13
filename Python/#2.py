'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = int(''.join(l1[::-1])) + int(''.join(l2[::-1]))
        return [int(n) for n in str(sum)[::-1]]

'Not working'

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def ListNodeGen(arr):
            if len(arr)==1:
                return ListNode(val=arr[0], next=None)
            return ListNode(val=arr[-1], next=ListNodeGen(arr[:-1]))

        s1 = []
        s2 = []
        while l1:
            s1.append(str(l1.val))
            l1 = l1.next
        while l2:
            s2.append(str(l2.val))
            l2 = l2.next
        summ = int(''.join(s1[::-1])) + int(''.join(s2[::-1]))
        nums = [int(n) for n in str(summ)]
        sol = ListNodeGen(nums)
        return sol

'''
Runtime: 84 ms, faster than 14.61% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next

'''
Runtime: 72 ms, faster than 54.16% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
'''
'''
In this last solution, dummy and cur "points" at the same object - ListNode(0) initially.
When I append a list to cur, it simultaneously appends to dummy as well, because they point at the same object.
However, when I do "cur = cur.next" - I'm just iterating my cur pointer down my object.
Both pointers are part of the same ListNode object, but cur pointer points one step ahead.
** LINKED List
'''
