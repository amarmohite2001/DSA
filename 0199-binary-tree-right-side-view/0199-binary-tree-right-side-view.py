# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q = collections.deque([root])
        while q:
            Rightside = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    #level 2- [2,3], Rightside =3
                    #level 3-[5,4], Rightside =4
                    Rightside=node
                    q.append(node.left)
                    q.append(node.right)
            if Rightside:
                res.append(Rightside.val)
        return res
            
            