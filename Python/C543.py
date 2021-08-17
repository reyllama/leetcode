"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        nodes = [root]
        
        def depth(node, d, left):
            if not node:
                return d-1
            if left:
                return max(depth(node.left, d+1, left=True), depth(node.left, d+1, left=False))
            else:
                return max(depth(node.right, d+1, left=True), depth(node.right, d+1, left=False))
        
        while nodes:
            node = nodes.pop()
            if node.left:
                nodes += [node.left]
            if node.right:
                nodes += [node.right]
            ans = max(ans, depth(node,0,left=True)+depth(node,0,left=False))
        return ans

"""
Runtime: 1652 ms, faster than 5.07% of Python online submissions for Diameter of Binary Tree.
Memory Usage: 16.1 MB, less than 86.26% of Python online submissions for Diameter of Binary Tree.
"""

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def depth(node):
            if not node: 
                return 0
            left, right = depth(node.left), depth(node.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
            
        depth(root)
        return self.ans

"""
Runtime: 36 ms, faster than 50.69% of Python online submissions for Diameter of Binary Tree.
Memory Usage: 16.3 MB, less than 18.56% of Python online submissions for Diameter of Binary Tree.
"""