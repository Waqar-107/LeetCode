# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:     
    def insertionSortList(self, head: ListNode) -> ListNode:
        ans = None
        
        while head:
            # insert the current head into the new list
            if ans == None:
                ans = ListNode(head.val)
            else:
                root = ans
                prev = None
                
                while root:
                    if root.val <= head.val and root.next == None:
                        x = ListNode(head.val)
                        root.next = x
                        break
                        
                    if root.val > head.val:
                        x = ListNode(head.val)
                        if prev:
                            prev.next = x
                            x.next = root
                            break
                        else:
                            x.next = root
                            ans = x
                            
                        break
                        
                    prev = root
                    root = root.next
                    
            head = head.next
            
        return ans
                
            
