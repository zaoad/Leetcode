# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = list()
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
            return
        
        dfs(root)
        min = None
        for i in range(len(nums)-1):
            if not min:
                min = nums[i+1] - nums[i]
            else:
                val = nums[i+1] - nums[i]
                if val<min:
                    min = val
        return min           
                    
