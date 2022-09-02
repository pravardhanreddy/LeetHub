ans = ["1"]
class Solution:
    def countAndSay(self, n: int) -> str:
        global ans
        
        if n <= len(ans):
            return ans[n-1]
        
        if n == len(ans) + 1:
            s = ans[-1]
            new = ""
            prev = s[0]
            count = 1
            for i in range(1,len(s)):
                if s[i] == prev:
                    count += 1
                else:
                    new += str(count) + prev
                    count = 1
                    prev = s[i]
            new += str(count) + prev
            ans.append(new)
            return new
        
        for i in range(len(ans), n+1):
            self.countAndSay(i)
        return ans[-1]
        