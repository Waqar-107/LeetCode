# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = None
        ret = None
        
        while head:
            temp = head.next
            flag = True
            
            while temp:
                if temp.val == head.val:
                    temp = temp.next
                    flag = False
                else:
                    break
            
            if flag:
                if not ans:
                    ans = head
                    ret = ans
                    ans.next = None
                else:
                    ans.next = head
                    ans = ans.next
                    if ans:
                        ans.next = None
            
            head = temp
        
        return ret