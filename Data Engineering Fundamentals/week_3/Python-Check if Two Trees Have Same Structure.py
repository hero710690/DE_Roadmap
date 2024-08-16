"""
Problem Statement
Given two binary trees, write a function to check if they are structurally identical. This means that both trees must have nodes at the same positions, and corresponding children (left and right) must exist in both trees.

Requirements
Both trees must be checked recursively to see if their structure (not the node values) matches.
Trees are considered structurally identical if:
Both trees are empty.
Both trees have a root node and the structure of their left and right subtrees are also identical.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True
    elif not tree1 or not tree2:
        return False
    
    return is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)

if __name__ == "__main__":
    # Example usage
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(4)
    tree2.left = TreeNode(5)
    tree2.right = TreeNode(6)

    tree3 = TreeNode(7)
    tree3.right = TreeNode(8)

    print(is_same_tree(tree1, tree2))  # True, because structure is the same
    print(is_same_tree(tree1, tree3))  # False, because structure differs
