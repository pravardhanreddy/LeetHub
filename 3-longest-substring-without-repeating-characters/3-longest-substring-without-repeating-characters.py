class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub  = set()
        maxlen = 0
        
        for i,n in enumerate(s):
            if n in sub:
                maxlen = max(maxlen, i-l)
                while(s[l] != n):
                    sub.discard(s[l])
                    l += 1
                sub.discard(s[l])
                l += 1
            sub.add(n)
        return max(maxlen, len(sub))
        
                