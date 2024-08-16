class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validateBinaryTree(root):
    visited = set()
    def dfs(node):
        if not node:
            return True
        if node in visited:
            return False
        return dfs(node.left) and dfs(node.right)
    return dfs(root)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

# This should return True as it's a valid binary tree
print(validateBinaryTree(node1))