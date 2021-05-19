"""
1261. Find Elements in a Contaminated Binary Tree

Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

You need to first recover the binary tree and then implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
bool find(int target) Return if the target value exists in the recovered binary tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = list()
        def recur(node):
            if node.left:
                node.left.val = 2*node.val+1
                self.vals.append(node.left.val)
                recur(node.left)
            if node.right:
                node.right.val = 2*node.val+2
                self.vals.append(node.right.val)
                recur(node.right)
        if root:
            root.val = 0
            self.vals.append(0)
            recur(root)
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        # for val in self.vals:
        #     if val == target:
        #         return True

        # return False

        return target in self.vals

"""
Runtime: 72 ms, faster than 93.55% of Python online submissions for Find Elements in a Contaminated Binary Tree.
Memory Usage: 20 MB, less than 87.10% of Python online submissions for Find Elements in a Contaminated Binary Tree.
"""

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# ["FindElements","find","find","find"]
# [[[-1,-1,-1,null,null,-1,-1,null,null,null,-1]],[6],[1],[6]]
# x = TreeNode(-1, TreeNode(-1), TreeNode(-1, TreeNode(-1), TreeNode(-1, None, TreeNode(-1))))
# obj = FindElements(x)
# param1 = obj.find(6)