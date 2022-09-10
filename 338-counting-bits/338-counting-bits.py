class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        
        for i in range(n+1):
            res = 0
            a = i
            while a:
                res += a%2
                a = a >> 1
                if dp[a] != 0:
                    dp[i] = dp[a] + res
                    break
                dp[i] = res
        return dp