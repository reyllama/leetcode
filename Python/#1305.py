"""
1305. All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        nodes = []

        def search(root):
            if root:
                search(root.left)
                nodes.append(root.val)
                search(root.right)

        search(root1)
        search(root2)

        return sorted(nodes)

"""
Runtime: 308 ms, faster than 95.02% of Python3 online submissions for All Elements in Two Binary Search Trees.
Memory Usage: 22.5 MB, less than 43.46% of Python3 online submissions for All Elements in Two Binary Search Trees.
"""
