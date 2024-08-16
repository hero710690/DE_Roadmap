from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_node = root

        if not root:
            return 
        self.invertTree(current_node.left)
        self.invertTree(current_node.right)
            
        tmp_node = current_node.right
        current_node.right = current_node.left
        current_node.left = tmp_node

        return root