# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        pushednode = 1
        ans =0
        while len(q) !=0:
            samelavelnode = pushednode
            pushednode = 0
            ans = 0
            for _ in range(samelavelnode):
                node = q.popleft()
                ans+=node.val
                if node.left is not None:
                    q.append(node.left)
                    pushednode+=1
                if node.right is not None:
                    q.append(node.right)
                    pushednode+=1
        return ans


