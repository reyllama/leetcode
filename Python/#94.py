"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node):
        if node:
            self.helper(node.left)
            self.res.append(node.val)
            self.helper(node.right)
        else:
            return None

"""
Runtime: 32 ms, faster than 58.35% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.8 MB, less than 52.53% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
