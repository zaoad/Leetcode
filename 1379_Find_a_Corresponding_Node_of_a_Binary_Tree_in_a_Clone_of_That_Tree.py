# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(t_origin, t_cloned):
            if t_origin == target:
                return t_cloned
            val1, val2 = None, None
            if t_origin.left != None:
                val1 = dfs(t_origin.left, t_cloned.left)
            if t_origin.right != None:
                val2 = dfs(t_origin.right, t_cloned.right)
            return val1 or val2
        dfs(original, cloned)

