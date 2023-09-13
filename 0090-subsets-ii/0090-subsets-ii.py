class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i=0):
            if i>=len(nums):
                a=sorted(subset)
                if a not in res:
                    res.append(a.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs()
        return res
            
            
        