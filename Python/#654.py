"""
654. Maximum Binary Tree

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        stack = []
        last = None

        for num in nums:
            n = TreeNode(val=num)
            while stack and stack[-1].val < num:
                last = stack.pop()
            if stack:
                stack[-1].right = n
            if last:
                n.left = last
            last = None
            stack.append(n)
        return stack[0]

"""
Runtime: 184 ms, faster than 94.73% of Python3 online submissions for Maximum Binary Tree.
Memory Usage: 14.8 MB, less than 88.70% of Python3 online submissions for Maximum Binary Tree.
"""
