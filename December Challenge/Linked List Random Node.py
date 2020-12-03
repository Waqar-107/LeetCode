# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        idx = random.random() * len(self.arr)
        return self.arr[int(idx)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
