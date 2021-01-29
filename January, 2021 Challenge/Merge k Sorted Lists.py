# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        arr = []
        for lst in lists:
            while lst:
                arr.append(lst.val)
                lst = lst.next
        
        if len(arr) == 0:
            return None
        
        arr.sort()
        
        root = ListNode(arr[0])
        head = root
        
        for i in range(1, len(arr)):
            head.next = ListNode(arr[i])
            head = head.next
        
        return root
        
        
        
