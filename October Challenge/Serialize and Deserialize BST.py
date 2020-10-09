# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if root == None:
            return ""
        
        q = []
        q.append(root)
        ret = str(root.val)
        
        while len(q):
            x = q.pop(0)
            
            if x.left:
                q.append(x.left)
                ret += "," + str(x.left.val)
            else:
                ret += ",-1"
                
            if x.right:
                q.append(x.right)
                ret += "," + str(x.right.val)
            else:
                ret += ",-1"
        
        return ret
        

    def deserialize(self, data: str) -> TreeNode:
        if len(data) == 0:
            return None
        
        arr = list(map(int, data.split(",")))
        
        root = TreeNode(arr[0])
        q = []
        q.append(root)
        arr.pop(0)
        
        while len(q):
            x = q.pop(0)
            
            uno = arr.pop(0)
            dos = arr.pop(0)
            
            if uno != -1:
                l = TreeNode(uno)
                x.left = l
                q.append(l)
                
            if dos != -1:
                r = TreeNode(dos)
                x.right = r
                q.append(r)
        
        return root
                
                
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
