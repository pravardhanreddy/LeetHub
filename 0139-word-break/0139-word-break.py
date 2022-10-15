class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        dp = [-1] * len(s)
        dp.append(True)
        
        def solution(start):
            if dp[start] != -1:
                return dp[start]
            
            for end in range(start, len(s)):
                if s[start:end+1] in d and solution(end+1):
                    dp[start] = True
                    return True
            dp[start] = False
            return False
        
        return solution(0)