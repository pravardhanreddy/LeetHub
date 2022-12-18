#User function Template for python3
import collections
class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        #return: count of sub-arrays having their sum equal to 0
        
        total = 0
        hm = collections.defaultdict(list)
        
        res = []
        
        for i in range(len(arr)):
            total += arr[i]
            
            if total == 0:
                res.append((0,i))
            
            if total in hm:
                for prev in hm[total]:
                    res.append((prev+1, i))
            
            hm[total].append(i)
        return len(res)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends