# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        self.pre_v = float('-inf')
        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left)
            if self.pre_v>=node.val:
                self.is_valid = False

            self.pre_v = node.val
            
            dfs(node.right)
        
        dfs(root)
        print(self.is_valid)
        return self.is_valid
    
if __name__=='__main__':
    sol = Solution()
    root = TreeNode(val= 5, left= TreeNode(val= 4, left=None, right= None), right= TreeNode(val= 6, left= TreeNode(val= 3, left= None, right= None), right= TreeNode(val= 7, left= None, right= None)))
    ans = sol.isValidBST(root) #ans = False