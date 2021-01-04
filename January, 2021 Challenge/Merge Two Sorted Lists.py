# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = None
        ans = None
        
        while l1 or l2:
            if not l1 and l2:
                if root:
                    root.next = l2
                    root = root.next
                else:
                    root = l2
                    ans = root
                l2 = l2.next
            
            elif not l2 and l1:
                if root:
                    root.next = l1
                    root = root.next
                else:
                    root = l1
                    ans = root
                l1 = l1.next
            
            else:
                if l1.val <= l2.val:
                    if root:
                        root.next = l1
                        root = root.next
                    else:
                        root = l1
                        ans = l1
                    
                    l1 = l1.next
                
                else:
                    if root:
                        root.next = l2
                        root = root.next
                    else:
                        root = l2
                        ans = l2
                    
                    l2 = l2.next
                    
        return ans
                    
