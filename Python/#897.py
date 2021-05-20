"""
897. Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        def in_order(node):
            if node:
                in_order(node.left)
                nodes.append(node.val)
                in_order(node.right)
        in_order(root)
        print(nodes)
        root = TreeNode(val=nodes.pop(0))
        cur = root
        while nodes:
            cur.right = TreeNode(val=nodes.pop(0))
            cur = cur.right
        return root

"""
Runtime: 20 ms, faster than 62.72% of Python online submissions for Increasing Order Search Tree.
Memory Usage: 13.6 MB, less than 47.39% of Python online submissions for Increasing Order Search Tree.
"""