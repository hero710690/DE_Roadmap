class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    
    max_sum = -float('inf')
    def calSum(node):
        nonlocal max_sum
        if not node:
           return 0
        
        current_left_sum = max(calSum(node.left), 0)
        current_right_sum = max(calSum(node.right),0)
        path_sum = node.val + current_left_sum + current_right_sum
        
        max_sum = max(max_sum, path_sum)
        return node.val + max(current_left_sum, current_right_sum)
    calSum(root)
    return max_sum

if __name__ == '__main__':
    # Example Usage
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    #    -10
    #   /  \
    #  9   20
    #     /  \
    #    15   7

    print(maxPathSum(root1))  # Output: 6
    print(maxPathSum(root2))  # Output: 42