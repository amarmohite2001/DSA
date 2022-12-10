class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # res = []
        # [res.append(i) for i in nums if i!=val]
#         for i in nums:
#             if i!=val:
#                 res.append(i)
#         return len(res)
        # k =0
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         nums[k]=nums[i]
        #         k+=1
        # return k    
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
