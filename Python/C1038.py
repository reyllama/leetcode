"""
1038. Binary Search Tree to Greater Sum Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        vals = []
        cur = root
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        
        def inorder_update(node):
            if not node:
                return
            inorder_update(node.left)
            node.val = vals.pop()
            inorder_update(node.right)
        
        inorder(root)
        vals = [sum(vals[i:]) for i in range(len(vals))][::-1]
        inorder_update(root)
        
        return root

"""
Runtime: 30 ms, faster than 12.73% of Python online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 13.4 MB, less than 62.42% of Python online submissions for Binary Search Tree to Greater Sum Tree.
"""

class Solution(object):
    val = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """        
        if root:
            self.bstToGst(root.right)
            root.val = self.val = root.val + self.val
            self.bstToGst(root.left)
        return root

"""
Runtime: 29 ms, faster than 12.73% of Python online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 13.6 MB, less than 32.12% of Python online submissions for Binary Search Tree to Greater Sum Tree.
"""