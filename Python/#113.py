"""
113. Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        res = []
        if not root:
            return res
        def dfs(cur, arr):
            if cur.left is None and cur.right is None:
                if sum(arr)==targetSum and len(arr)>0:
                    res.append(arr)
                return
            if cur.left:
                dfs(cur.left, arr+[cur.left.val])
            if cur.right:
                dfs(cur.right, arr+[cur.right.val])
        dfs(root, [root.val])
        
        return res

"""
Runtime: 32 ms, faster than 90.54% of Python online submissions for Path Sum II.
Memory Usage: 19.5 MB, less than 31.09% of Python online submissions for Path Sum II.
"""
