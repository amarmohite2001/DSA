# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return root
        while root is not None and root.val is not None:
            if val < root.val:
                root = root.left
            elif val>root.val:
                root = root.right
            else:
                return root
        # return root
                
        
        
        