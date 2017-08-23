// *** Not working file only functional method ***

// Source https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
// Given the root node of a binary tree, can you determine if it's also a binary search tree?
/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
     }
*/
boolean checkBST(Node root) {
    if (root == null) {
        return false;
    } else {
        return treeIsBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
}

boolean treeIsBST(Node node, int min, int max) {
    if (node.left == null && node.right == null) {
        return true;
    } else {
        boolean isBST = true;
        if (node.left != null) {
            if (nodeInRange(node.left, min, node.data)) {
                isBST = isBST && treeIsBST(node.left, min, node.data);
            } else {
                return false;
            }
        }
        if (node.right != null) {
            if (nodeInRange(node.right, node.data, max)) {
                isBST = isBST && treeIsBST(node.right, node.data, max);
            } else {
                return false;
            }
        }
        return isBST;
    }
}

boolean nodeInRange(Node node, int min, int max) {
    if (node.data < max && node.data > min) {
        return true;
    } else {
        return false;
    }
}
