#User function Template for python3
from collections import defaultdict
# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        ans = set()
        hm = defaultdict(list)
        for a in range(len(arr)):
            for b in range(a+1, len(arr)):
                hm[arr[a] + arr[b]].append((a,b))
        
        for c in range(len(arr)):
            for d in range(c+1, len(arr)):
                if (k-arr[c]-arr[d]) in hm:
                    for a, b in hm[k-arr[c]-arr[d]]:
                        if c!=a and c!=b and d!=a and d!=b:
                            quad = [arr[a],arr[b],arr[c],arr[d]]
                            quad.sort()
                            ans.add(tuple(quad))
        return sorted(list(ans))
                            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends