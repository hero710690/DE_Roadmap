# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:  
            return None  
        root_val = preorder[0]
        root = TreeNode(val=preorder[0])
        root_index = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root
    
if __name__ == "__main__": 
    inorder = [9,3,15,20,7]
    preorder = [3,9,20,15,7]
    sol = Solution()
    ans =  sol.buildTree(preorder, inorder)
