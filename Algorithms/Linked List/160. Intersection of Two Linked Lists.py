# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cnt1 = cnt2 = 0
        
        A = headA
        B = headB
        
        while A:
            cnt1 += 1
            A = A.next
        
        while B:
            cnt2 += 1
            B = B.next
        
        A = headA
        B = headB
        
        while cnt1 > cnt2:
            cnt1 -= 1
            A = A.next
        
        while cnt2 > cnt1:
            cnt2 -= 1
            B = B.next
        
        while A and B:
            if A == B:
                return A
            
            A = A.next
            B = B.next
        
        return None