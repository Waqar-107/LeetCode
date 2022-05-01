"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def solve(self, head):
        if not head:
            return head
        
        if head.next == None and head.child == None:
            return head
        
        if head.next == None and head.child:
            head.next = head.child
            head.child.prev = head
            head.child = None
            return self.solve(head)
        
        if head.next and head.child == None:
            return self.solve(head.next)
        
        # head has both next and child
        # save the next, make the child, heads, next. solve for it
        # then whatever the solve returns, make its next equal to the saved var
        # solve for the saved
        temp_node = head.next
        head.next = head.child
        head.child.prev = head
        head.child = None
        
        res = self.solve(head.next)
        
        # res can't be null, if it is then probably sth is wrong in my code :v
        res.next = temp_node
        temp_node.prev = res
        return self.solve(temp_node)
    
    def flatten(self, head: 'Node') -> 'Node':
        self.solve(head)
        return head
    
