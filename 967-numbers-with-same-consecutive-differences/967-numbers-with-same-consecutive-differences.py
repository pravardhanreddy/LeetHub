class Solution:
    def numsSameConsecDiff(self, n,k):
        def solve(f, n, k):
            if n == 0:
                return ['']
            ans = []
            if f + k <= 9:
                res = solve(f+k, n-1, k)
                strf = str(f+k)
                for s in res:
                    ans.append(strf+s)
            if f - k >= 0:
                res = solve(f-k, n-1, k)
                strf = str(f-k)
                for s in res:
                    ans.append(strf+s)
            return ans
        
        result = []
        if k == 0:
            for i in range(1,10):
                result.append(int(str(i)*n))
            return result
        
        for i in range(1,10):
            res = solve(i, n-1, k)
            for r in res:
                result.append(int(str(i)+r))
        return result