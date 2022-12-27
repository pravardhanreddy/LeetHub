#User function Template for python3

#User function Template for python3

class Solution:
    def rremove (self, s):
        #code here
        ans = []
        
        i = 0
        while i < len(s):
            if i == len(s)-1 or s[i] != s[i+1]:
                ans.append(s[i])
                i += 1
            else:
                while i+1 < len(s) and s[i+1] == s[i]:
                    i += 1
                i += 1
        ans = ''.join(ans)
        if ans == s:
            return ans
            
        return self.rremove(ans)
              

		      


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends