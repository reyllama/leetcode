"""
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums, lo=-1, hi=10**4+1):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if hi > 10**4:
            hi = len(nums)
        if hi<=lo+1:
            return
        idx = lo + (hi-lo)//2
        root = TreeNode(val=nums[idx])
        root.left = self.sortedArrayToBST(nums, lo=lo, hi=idx)
        root.right = self.sortedArrayToBST(nums, lo=idx, hi=hi)
        return root

"""
Runtime: 48 ms, faster than 72.22% of Python online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16 MB, less than 94.05% of Python online submissions for Convert Sorted Array to Binary Search Tree.
"""