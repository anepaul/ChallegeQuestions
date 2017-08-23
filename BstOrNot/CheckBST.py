# Source https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
# Given the root node of a binary tree, can you determine if it's also a binary search tree?

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    if root is None:
        return False
    else:
        return treeIsBST(root, 0, 10**4)

def treeIsBST(node, min_val, max_val):
    # Sanity check
    if node is None:
        raise ValueError("Node parameter must not be None")

    # Is leaf node
    if node.left is None and node.right is None:
        return True

    # Not leaf
    isBST = True
    if node.left is not None:
        # Node must be greater than minimum value and less than current node
        # Otherwise this is not a BST
        if nodeInRange(node.left, min_val, node.data):
            isBST = isBST and treeIsBST(node.left, min_val, node.data)
        else:
            return False
    
    if node.right is not None:
        # Node must be greater than current node and less than maximum value
        # Otherwise this is not a BST
        if nodeInRange(node.right, node.data, max_val):
            isBST = isBST and treeIsBST(node.right, node.data, max_val)
        else:
            return False
    
    return isBST

""" Returns True if Node's data is within min and max, otherwise Falsed
"""
def nodeInRange(node, min_val, max_val):
    # Sanity check
    if node is None:
        raise ValueError("Node parameter must not be None")

    if node.data > min_val and node.data < max_val:
        return True
    else:
        return False