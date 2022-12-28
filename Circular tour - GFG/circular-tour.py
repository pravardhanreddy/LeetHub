'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        i = 0
        ans = -1
        while i < n:
            j = 0
            s = 0
            while j < n:
                ind = (i+j)%n
                s += lis[ind][0] - lis[ind][1]
                if s < 0:
                    break
                j += 1
            
            if j == n:
                ans = i
                break
            i += j+1
            
        return ans


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends