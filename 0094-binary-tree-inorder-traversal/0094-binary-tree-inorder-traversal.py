# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        def inorder(curr):
            if curr.left is not None:
                inorder(curr.left)
            res.append(curr.val)
            if curr.right is not None:
                inorder(curr.right)
        if not root:
            return None
        inorder(root)
        return res
        