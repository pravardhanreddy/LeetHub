from collections import defaultdict
from typing import List
class Solution:
    def findMinTime(self, n : int, l : int, arr : List[int]) -> int:
        # code here
        d = defaultdict(int)
        for i in range(l):
            t = 0
            k = 1
            while k <= n:
                d[t + arr[i]*k]+= 1
                t += arr[i]*k
                k += 1
        s = 0
        t = 0
        for i in sorted(d.keys()):
            s += d[i]
            if s >= n:
                t = i
                break
        return t



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        l = int(input())
        
        
        arr=IntArray().Input(l)
        
        obj = Solution()
        res = obj.findMinTime(n, l, arr)
        
        print(res)
        

# } Driver Code Ends