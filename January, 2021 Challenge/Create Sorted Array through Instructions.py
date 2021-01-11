from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        lst = SortedList()
        ans = 0
        n = len(instructions)
        
        for i in range(n):
            ans += min(lst.bisect_left(instructions[i]), len(lst) - lst.bisect_right(instructions[i]))
            ans %= (10**9 + 7)
            
            lst.add(instructions[i])
        
        return ans
