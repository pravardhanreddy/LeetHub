#User function Template for python3

class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        d = set(dictionary)
        st = set()
        r = len(board)
        c = len(board[0])
        for word in dictionary:
            for i in range(len(word)):
                st.add(word[:i+1])
        
        ans = []
        
        def dfs(i,j,s):
            if i>=r or i < 0 or j >= c or j < 0:
                return
            
            s += board[i][j]
            if s not in st:
                return
            
            if s in d:
                ans.append(s)

            store = board[i][j]
            board[i][j] = '*'
            
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    dfs(i+x, j+y, s)
            
            board[i][j] = store
        
        for i in range(r):
            for j in range(c):
                dfs(i,j,'')
        ans = list(set(ans))
        ans.sort()
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        N=int(input())
        dictionary=[x for x in input().strip().split()]
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        board=[]
        for _ in range(R):
            board.append( [x for x in input().strip().split()] )
        obj = Solution()
        found = obj.wordBoggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()                               # sorting output
        for i in found:
            print(i,end=' ')
        print()
# } Driver Code Ends