#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        d = {}
        x = 0
        ans = 0
        for i in range(n):
            if x in d:
                d[x]+=1
            else:
                d[x] = 1
            if(arr[i]):
                x+=1
            else:
                x-=1
            if x in d:
                ans += d[x]
        return ans
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends