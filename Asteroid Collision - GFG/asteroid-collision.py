#User function Template for python3

class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        pos = []
        neg = []
        
        for i,ast in enumerate(asteroids):
            # print(pos, neg)
            if ast > 0:
                pos.append((i,ast))
            else:
                while pos and -ast > pos[-1][1]:
                    last = pos.pop()
                if pos and -ast == pos[-1][1]:
                    last = pos.pop()
                    continue
                if not pos:
                    neg.append((i,ast))
        # print(pos, neg)
        comb = sorted(pos + neg)
        ans = []
        for _,val in comb:
            ans.append(val)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends