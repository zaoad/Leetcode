# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: [TreeNode]):
        self.next_index = -1
        self._stack = list()
        self.head = None
        for val in root:
            if val is None:
                continue
            if self.head is None:
                self.head = TreeNode(val)
                continue
            self._insertBST(val)
        self._inOrder(self.head)

    def next(self) -> int:
        self.next_index +=1
        return self._stack[self.next_index]

    def hasNext(self) -> bool:
        if self.next_index+1 >= len(self._stack):
            return False
        return True

    def _insertBST(self, val) -> None:
        temp_head = self.head
        while temp_head:
            if val <= temp_head.val:
                if temp_head.left == None:
                    temp_head.left = TreeNode(val)
                    break;
                else:
                    temp_head = temp_head.left
            else:
                if temp_head.right == None:
                    temp_head.right = TreeNode(val)
                    break;
                else:
                    temp_head = temp_head.right

    def _inOrder(self, node):
        if not node:
            return;
        self._inOrder(node.left)
        # print(node.val)
        self._stack.append(node.val)
        self._inOrder(node.right)

bSTIterator = BSTIterator([7, 3, 15, None, None, 9, 20]);
print(bSTIterator.next());
print(bSTIterator.next());
print(bSTIterator.hasNext());
print(bSTIterator.next());
print(bSTIterator.hasNext());
print(bSTIterator.next());
print(bSTIterator.hasNext());
print(bSTIterator.next());
print(bSTIterator.hasNext());
