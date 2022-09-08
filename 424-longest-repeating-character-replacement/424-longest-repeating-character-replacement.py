class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        l = 0
        mostf = 0
        count = Counter()
        res = 0
        
        for r in range(len(s)):
            count[s[r]] += 1
            
            mostf = max(mostf, count[s[r]])
            if (r-l+1) - mostf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
                
                