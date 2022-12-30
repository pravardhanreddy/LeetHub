#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def NumberOFTurns(self, root, first, second):
        #return the number of turns required to go from first node to second node
        d1 = set()
        d2 = set()
        
        def dfs(root, target, d):
            if not root:
                return
            if root.data == target:
                d.add(root)
                return
            dfs(root.left, target, d)
            if root.left in d:
                d.add(root)
                return
            dfs(root.right, target, d)
            if root.right in d:
                d.add(root)
                return
        
        dfs(root, first, d1)
        dfs(root, second, d2)
        
        d = d1.intersection(d2)
        node = root
        while True:
            if node.left in d:
                node = node.left
            elif node.right in d:
                node = node.right
            else:
                break
        def turns(node, target, d):
            if node.data == target:
                return 0
            side = 0 # left
            if node.right in d:
                side = 1 # right
            cnt = 0
            while node.data != target:
                if node.left in d:
                    if side == 1:
                        cnt += 1
                        side = 0
                    node = node.left
                elif node.right in d:
                    if side == 0:
                        cnt += 1
                        side = 1
                    node = node.right
            return cnt
        if node.data == first:
            return turns(node, second, d2)
        if node.data == second:
            return turns(node, first, d1)
        return turns(node, first, d1) + turns(node, second, d2) + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        n1,n2=list(map(int, input().strip().split())) 
        ob = Solution()
        turn = ob.NumberOFTurns(root,n1,n2)
        if turn!=0:
            print(turn)
        else:
            print(-1)
# } Driver Code Ends