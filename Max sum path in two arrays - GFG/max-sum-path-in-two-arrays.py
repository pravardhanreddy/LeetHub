#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxSumPath(self, arr1, arr2, m, n):
        #code here
        i,j = 0,0
        s1, s2 = 0,0
        ans = 0
        while(i<m and j<n):
            if arr1[i] == arr2[j]:
                ans += max(s1,s2) + arr1[i]
                s1,s2 = 0,0
                i+=1
                j+=1
            elif arr1[i] < arr2[j]:
                s1 += arr1[i]
                i += 1
            else:
                s2 += arr2[j]
                j += 1
        if i < m:
            while(i<m):
                s1 += arr1[i]
                i += 1
        elif j < n:
            while(j<n):
                s2 += arr2[j]
                j += 1
        ans += max(s1,s2)
        return ans

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        m,n = list(map(int, input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        print(Solution().maxSumPath(arr1, arr2, m, n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends