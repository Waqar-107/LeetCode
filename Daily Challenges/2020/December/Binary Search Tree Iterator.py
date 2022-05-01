# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.inorder(root)
        
    
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.right)
        self.stack.append(root)
        self.inorder(root.left)

    def next(self) -> int:
        x = self.stack.pop()
        return x.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
