from collections import deque
from typing import Optional, List
# LeetCode: https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        queue = []
        result = []
        queue = deque([root])
        
        while len(queue)>0:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                if i==level_size-1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    