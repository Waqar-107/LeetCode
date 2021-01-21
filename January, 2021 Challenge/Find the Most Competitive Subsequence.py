class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        allowed_to_rem = len(nums) - k
        
        for n in nums:
            while len(stack) and stack[-1] > n and allowed_to_rem > 0:
                stack.pop()
                allowed_to_rem -= 1
            
            stack.append(n)
        
        return stack[:k]
