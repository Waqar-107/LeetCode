# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.val = 0
        
    def assignDigit(self, root):
        if root == None:
            return
        
        if root.next:
            self.assignDigit(root.next)
        
        root.val = self.val % 10
        self.val //= 10
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cnt1 = 0
        cnt2 = 0
        
        head = l1
        while head:
            cnt1 += 1
            head = head.next
        
        head = l2
        while head:
            cnt2 += 1
            head = head.next
        
        ans = 0
        p = 1
        
        h1 = l1
        h2 = l2
        if cnt1 > cnt2:
            for i in range(cnt1 - cnt2):
                ans = ans * 10 + h1.val
                h1 = h1.next
        elif cnt2 > cnt1:
            for i in range(cnt2 - cnt1):
                ans = ans * 10 + h2.val
                h2 = h2.next
        
        while h1 and h2:
            ans = ans * 10 + h1.val + h2.val
            h1 = h1.next
            h2 = h2.next
        
        self.val = ans
        
        ansNode = None
        if cnt1 > cnt2:
            self.assignDigit(l1)
            ansNode = l1
        else:
            self.assignDigit(l2)
            ansNode = l2
        
        if self.val > 0:
            newNode = ListNode(self.val, ansNode)
            return newNode
        
        return ansNode
            
        