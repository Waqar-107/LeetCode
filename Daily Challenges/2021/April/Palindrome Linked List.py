# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, root):
        if not root:
            return None
        
        if root.next == None:
            return root
        
        ret = self.rev(root.next)
        root.next.next = root
        root.next = None
        
        return ret
    
    def isPalindrome(self, head: ListNode) -> bool:
        cnt = 0
        
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        
        idx = 0
        if cnt % 2:
            target = cnt // 2 + 1
        else:
            target = cnt // 2
            
        # reverse from start to last
        temp = head
        head2 = None
        
        # create a new head. let the middle node point to null
        while temp:
            idx += 1
            
            if idx == target:
                head2 = temp.next
                temp.next = None
                break
            
            temp = temp.next
        
        head2 = self.rev(head2)

        # now check for palindrome
        while head and head2:
            if head.val == head2.val:
                head = head.next
                head2 = head2.next
                continue
            
            return False
        
        return True
