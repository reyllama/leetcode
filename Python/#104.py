"""
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)

            return ldepth+1 if ldepth>rdepth else rdepth+1
        return 0

"""
Runtime: 48 ms, faster than 42.86% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.4 MB, less than 53.07% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
