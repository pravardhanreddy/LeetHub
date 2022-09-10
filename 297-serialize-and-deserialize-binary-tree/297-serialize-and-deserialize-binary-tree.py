# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = root
        if not root:
            return ''
        ans = ''
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                ans += ','
                continue
            ans += str(node.val) + ','
            q.append(node.left)
            q.append(node.right)
        return ans
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        q = deque()
        i = 0
        head = None
        s = ''
        while data[i] != ',':
            s += data[i]
            i+=1
        
        i+=1
        
        head = TreeNode(int(s))
        q.append(head)
        
        while i < len(data):
            node = q.popleft()
            
            # left
            s = ''
            while i < len(data) and data[i] != ',':
                s += data[i]
                i+=1
            i += 1
            if s:
                node.left = TreeNode(int(s))
                q.append(node.left)
            
            # right
            s = ''
            while i < len(data) and data[i] != ',':
                s += data[i]
                i+=1
            i += 1
            if s:
                node.right = TreeNode(int(s))
                q.append(node.right)
            
        return head
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))