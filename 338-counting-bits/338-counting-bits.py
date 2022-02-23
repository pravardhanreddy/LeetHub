class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            t = format(i,"b")
            ans.append(t.count("1"))
        return ans