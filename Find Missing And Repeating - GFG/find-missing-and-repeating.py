#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        s1 = sum(arr)
        s2 = sum([a*a for a in arr])
        s = (n*(n+1))//2 - s1
        ss = (n*(n+1)*(2*n+1)) // 6 - s2
        
        a = ((ss//s) + s) // 2
        b = a - s
        return [b,a]
        
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends