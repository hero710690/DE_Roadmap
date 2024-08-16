# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cnt = 0
        stack = []
        current = root
        
        while True:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            cnt+=1
            if cnt==k:
                return current.val
            
            current = current.right

if __name__ == '__main__':
    # Example usage:
    root = TreeNode(val=3, left=TreeNode(val=1, right=TreeNode(val=2)), right=TreeNode(val=4))
    k=1
    sol = Solution()
    ans = sol.kthSmallest(root,k) #ans = 1
    print(ans)
