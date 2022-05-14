# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self._stack = list()
        self._first = None
        self._second = None
        self._index = -1
        self._inOrder(root)
        self._find_diff()
        # print('an', self._first.val, self._second.val)
        if not self._second:
            self._second = self._stack[self._index]
        temp = self._first.val
        self._first.val = self._second.val
        self._second.val = temp

    def _inOrder(self, node):
        if not node:
            return;
        self._inOrder(node.left)
        self._stack.append(node)
        self._inOrder(node.right)

    def _find_diff(self):

        for i in range(1, len(self._stack)):
            n1 = self._stack[i - 1]
            n2 = self._stack[i]
            # print(n1.val, n2.val)
            if n1.val > n2.val:
                # print('d')
                if self._first is None:
                    # print('k')
                    self._index = i
                    self._first = n1
                else:
                    # print('m')
                    self._second = n2

