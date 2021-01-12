# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = None
        root = None
        
        carry = 0
        while l1 or l2:
            if l1 and not l2:
                val = carry + l1.val
                l1 = l1.next
                
            elif l2 and not l1:
                val = carry + l2.val
                l2 = l2.next
            
            else:
                val = carry + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            
            # update the value
            if root == None:
                root = ListNode(val % 10)
                ans = root
            else:
                root.next = ListNode(val % 10)
                root = root.next
                
            carry = val // 10
        
        if carry:
            root.next = ListNode(carry)    
        
        return ans
        
