class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j= 0,len(height)-1
        volume_tracker = 0
        while i<=j:
            length = j-i
            h = min(height[i], height[j])
            if volume_tracker < length*h:
                volume_tracker= length*h
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return volume_tracker
            
            
        