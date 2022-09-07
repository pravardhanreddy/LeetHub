class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxvol = 0
        
        l,r = 0, len(height) - 1
        
        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            maxvol = max(maxvol, vol)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        return maxvol