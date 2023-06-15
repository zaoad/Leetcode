# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((root, 1))
        max, sum, current_level, max_level = float('-inf'), 0, 1, 1
        cur_l = 0
        while len(q) != 0:
            cur, cur_l = q.popleft()
            if cur_l == current_level:
                sum += cur.val
            else:
                if sum > max:
                    max = sum
                    max_level = current_level
                current_level = cur_l
                sum = cur.val
            if cur.left:
                q.append((cur.left, cur_l+1))
            if cur.right:
                q.append((cur.right, cur_l+1))
        if sum > max:
            max = sum
            max_level = cur_l
        return max_level
        
