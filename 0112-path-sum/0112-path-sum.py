# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: If the root is None, there's no path to check.
            if root is None:
                return False

            # Subtract the current node's value from the targetSum.
            targetSum -= root.val

            # If it's a leaf node and the targetSum is 0, we found a path.
            if root.left is None and root.right is None:
                return targetSum == 0

            # Recursively check the left and right subtrees.
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)