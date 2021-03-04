# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cnt1 = 0
        cnt2 = 0
        
        temp = headA
        while temp:
            cnt1 += 1
            temp = temp.next
        
        temp = headB
        while temp:
            cnt2 += 1
            temp = temp.next
        
        while cnt1 > cnt2:
            headA = headA.next
            cnt1 -= 1
        
        while cnt2 > cnt1:
            headB = headB.next
            cnt2 -= 1
        
        while headA and headB:
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
        
        return None
