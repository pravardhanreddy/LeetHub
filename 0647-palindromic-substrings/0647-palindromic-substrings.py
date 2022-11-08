class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        
        for i in range(len(s)):
            # expand from i on either side
            
            # odd case
            
            k = 1
            while i-k >= 0 and i+k < len(s) and s[i-k] == s[i+k]:
                ans += 1
                k += 1
            
            # even case
            
            k = 1
            while i-k+1>=0 and i+k < len(s) and s[i-k+1] == s[i+k]:
                ans += 1
                k += 1
        return ans