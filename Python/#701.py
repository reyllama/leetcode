"""
701. Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if not root:
            return TreeNode(val)

        def helper(start, val):
            if start.val > val:
                if start.left:
                    return helper(start.left, val)
                else:
                    start.left = TreeNode(val)
            else:
                if start.right:
                    return helper(start.right, val)
                else:
                    start.right = TreeNode(val)

        helper(root, val)

        return root

"""
Runtime: 120 ms, faster than 98.69% of Python online submissions for Insert into a Binary Search Tree.
Memory Usage: 17.8 MB, less than 11.11% of Python online submissions for Insert into a Binary Search Tree.
"""