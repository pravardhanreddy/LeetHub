class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        
        maxL, maxR = height[l], height[r]
        
        ans = 0
        
        while l <= r:
            if maxL < maxR:
                maxL = max(maxL, height[l])
                ans += maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                ans +=maxR - height[r]
                r -= 1
        return ans
                
        