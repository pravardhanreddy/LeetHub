#User function Template for python3

class Solution:
    def wordBreak(self, n, d, s):
        # code here
        d = set(d)
        pre = set()
        for word in d:
            for i in range(1,len(word)+1):
                pre.add(word[:i])
        
        def count(s):
            # if len(s) == 0:
            #     return ['']
            
            ans = []
            
            for i in range(1,len(s)+1):
                word = s[:i]
                if word not in pre:
                    break
                
                if word in d:
                    if i == len(s):
                        return ans+[word]
                    l = count(s[i:])
                    for sentence in l:
                        ans.append(word + ' ' + sentence)
                    
            
            return ans
        
        
        return count(s)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dicti = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dicti, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends