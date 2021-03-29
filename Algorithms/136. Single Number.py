class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = nums[0]
        
        for i in range(1, len(nums)):
            b = b ^ nums[i]
        
        return b
