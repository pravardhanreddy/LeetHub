class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        
        maxL, maxR = height[l], height[r]
        
        ans = 0
        
        while l <= r:
            if maxL < maxR:
                ans += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
                l += 1
            else:
                ans += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
                r -= 1
        return ans
                
        