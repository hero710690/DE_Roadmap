# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Define a Node class to represent nodes in the binary search tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function to find the lowest common ancestor (LCA) of two nodes in a binary search tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            # Check if both nodes are in the left subtree
            if node.val > p.val and node.val>q.val:
                return dfs(node.left)
            # Check if both nodes are in the right subtree
            elif node.val<p.val and node.val< q.val:
                return dfs(node.right)
            # If the above conditions are not met, the current root is the LCA
            else:
                return node
        anc = dfs(root)
        return anc
if __name__ == '__main__':
    # Example usage:
    # Create a sample binary search tree
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)
    root.right.right = TreeNode(35)

    # Initialize two nodes to find their lowest common ancestor
    node1 = TreeNode(5)
    node2 = TreeNode(15)

    # Find the lowest common ancestor of the two nodes in the BST
    sol = Solution()
    lca_node = sol.lowestCommonAncestor(root, node1, node2)
    print("Lowest Common Ancestor:", lca_node.val)