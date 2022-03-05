#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        z,o,t = 0,0,0
        
        for a in arr:
            if a == 0:
                z += 1
            elif a == 1:
                o += 1
            elif a==2:
                t += 1
        
        arr[0:z] = [0]*z
        arr[z:z+o] = [1]*o
        arr[z+o:] = [2]*t
        
        return arr
        
        
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends