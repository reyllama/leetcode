"""
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:

        ans = []

        n -= 1

        if n == 0:
            return [TreeNode(0)]

        for i in range(1, min(n, 20), 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n-i):
                    root = TreeNode()
                    root.left = left
                    root.right = right
                    ans.append(root)

        return ans

"""
Runtime: 324 ms, faster than 16.18% of Python3 online submissions for All Possible Full Binary Trees.
Memory Usage: 27.6 MB, less than 8.96% of Python3 online submissions for All Possible Full Binary Trees.
"""
