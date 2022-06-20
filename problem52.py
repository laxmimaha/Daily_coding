"""
Suppose an arithmetic expression is given as a binary tree. 
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).

"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def evaluateTree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.val)
    if root.val == '+':
        return evaluateTree(root.left) + evaluateTree(root.right)
    elif root.val == '-':
        return evaluateTree(root.left) - evaluateTree(root.right)
    elif root.val == '*':
        return evaluateTree(root.left) * evaluateTree(root.right)
    else:
        return evaluateTree(root.left) / evaluateTree(root.right)

root = TreeNode('+')
root.left = TreeNode('*')
root.left.left = TreeNode('5')
root.left.right = TreeNode('10')
root.right = TreeNode('*')
root.right.left = TreeNode('10')
root.right.right = TreeNode('6')

print(evaluateTree(root))
print(root)