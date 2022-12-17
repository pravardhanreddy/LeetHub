
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        lmax = arr[0]
        rmax = arr[-1]
        
        l,r = 1,n-2
        res = 0
        while l <= r:
            if lmax < rmax:
                lmax = max(lmax,arr[l])
                res += lmax - arr[l]
                l += 1
            else:
                rmax = max(rmax, arr[r])
                res += rmax - arr[r]
                r -= 1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends