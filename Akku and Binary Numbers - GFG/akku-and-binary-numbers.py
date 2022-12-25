#User function Template for python3

class Solution:
    def solve (self, L, r):
        
        # code here
        if r < 7:
            return 0
            
        cnt = 0
        
        lstr = str(bin(L))[2:]
        rstr = str(bin(r))[2:]
        
        llen = len(lstr)
        rlen = len(rstr)
        
        i = (1 << (llen-1)) if L > 4 else 4
        # print(i, )
        while i <= r:
            j = 2
            while (j < i) and (i|j) <= r:
                k = 1
                while k < j and (i|j|k) <= r:
                    if L <= (i|j|k) <= r:
                        cnt += 1
                    k <<= 1
                j <<= 1
            i <<= 1
        return cnt
        
        
        
        print(lstr, rstr)
        
    def precompute (self):
        pass
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    ob.precompute()
    t = int (input ())
    for _ in range (t):
        L, R = map(int,input().split())
        ans = ob.solve(L, R);
        print(ans)




# } Driver Code Ends