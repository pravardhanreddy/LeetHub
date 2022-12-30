#User function Template for python3

class Solution: 
    def minLaptops(self, N, start, end):
        # Code here
        ans = 0
        cnt = 0
        comb = list(zip(start, [1]*N))
        comb += list(zip(end, [0]*N))
        
        comb.sort()
        
        for t,s in comb:
            if s == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt -= 1
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        start = list(map(int,input().split()))
        end = list(map(int,input().split()))
            
        ob = Solution()
        print(ob.minLaptops(N, start, end))
        
        T -= 1

# } Driver Code Ends