"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def switch(node):
            if node:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                switch(node.left)
                switch(node.right)
            else:
                return
        switch(root)
        return root

"""
Runtime: 8 ms, faster than 99.60% of Python online submissions for Invert Binary Tree.
Memory Usage: 13.4 MB, less than 76.35% of Python online submissions for Invert Binary Tree.
"""