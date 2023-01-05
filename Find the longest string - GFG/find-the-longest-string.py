#User function Template for python3

def check(s, a):
    for i in range(n-1, -1, -1):
        if a[:i] not in s:
            # print(a[:i])
            return False
    return True

class Solution():
    def longestString(self, arr, n):
        #your code goes here
        arr.sort()
        s = set()
        ans = ''
        s.add('')
        for a in arr:
            # print(a)
            s.add(a)
            if check(s,a):
                if len(a) > len(ans) or (len(a) == len(ans) and a < ans):
                    ans = a
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends