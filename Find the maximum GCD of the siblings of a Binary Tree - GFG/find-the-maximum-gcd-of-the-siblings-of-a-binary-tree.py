'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

    '''
def gcd(a, b):
 
    if (a == b):
        return a
 
    # GCD(0, b) == b; GCD(a, 0) == a,
    # GCD(0, 0) == 0
    if (a == 0):
        return b
 
    if (b == 0):
        return a
 
    # look for factors of 2
    # a is even
    if ((~a & 1) == 1):
 
        # b is odd
        if ((b & 1) == 1):
            return gcd(a >> 1, b)
        else:
            # both a and b are even
            return (gcd(a >> 1, b >> 1) << 1)
 
    # a is odd, b is even
    if ((~b & 1) == 1):
        return gcd(a, b >> 1)
 
    # reduce larger number
    if (a > b):
        return gcd((a - b) >> 1, b)
 
    return gcd((b - a) >> 1, a)

# from collections import deque
class Solution:
    def maxGCD(self, root):
        # code here
        if not root:
            return -1
        
        ans = [0, None]
        def dfs(ans, root):
            if not root:
                return
            if root.left and root.right:
                g = gcd(root.left.data, root.right.data)
                if g > ans[0]:
                    ans[0] = g
                    ans[1] = root.data
                elif g == ans[0]:
                    ans[1] = max(ans[1], root.data)
            dfs(ans, root.left)
            dfs(ans, root.right)
        dfs(ans, root)
        return ans[1] if ans[1] else 0


#{ 
 # Driver Code Starts
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.maxGCD(root))
        
        


# } Driver Code Ends