# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            # Return an empty list if the node is None, signaling the end of a path
            if not node:
                return []
            # Identify leaf nodes (nodes without children)
            if not node.left and not node.right:
                # Return a list with one element, 1 at index 0 indicating a leaf at distance 0
                return [1]
            # Recursively find the distance array for the left and right subtrees
            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            # Calculate the number of good leaf pairs between the left and right subtrees
            for i in range(len(left_dist)):
                for j in range(len(right_dist)):
                    # Check if the sum of distances and two (for the edges connecting to the current node) is within the allowed distance
                    if i+j+2 <= distance:
                        # Accumulate the result with the product of the number of leaves at these distances
                        nonlocal result
                        result += left_dist[i] * right_dist[j]

            # Create a new distances array to return to the parent node
            new_distances = [0] * (distance + 1)
            # Update each distance count based on the distances from the current node's children
            for i in range(1, len(new_distances)):
                # Increment distances by 1 (moving up the tree), check bounds to avoid index errors
                new_distances[i] = (left_dist[i-1] if i-1 < len(left_dist) else 0) + \
                                    (right_dist[i-1] if i-1 < len(right_dist) else 0)
            
            # Return the updated distances to the parent
            return new_distances
        
        result = 0
        dfs(root)
        return result

if __name__ == '__main__':
    # Example usage:
    # Create a sample binary search tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    distance = 3
    # Find the lowest common ancestor of the two nodes in the BST
    sol = Solution()
    ans = sol.countPairs(root, distance) #ans = 2
    print(ans)