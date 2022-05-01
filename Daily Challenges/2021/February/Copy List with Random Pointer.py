"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        nodes = defaultdict(Node)
        
        temp = head
        while temp:
            nodes[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        new_head = nodes[head]
        
        while temp:
            if temp.next:
                nodes[temp].next = nodes[temp.next]
            
            if temp.random:
                nodes[temp].random = nodes[temp.random]
            
            temp = temp.next
            
        return new_head
