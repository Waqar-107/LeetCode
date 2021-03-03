class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        exp = 0
        
        for i in range(len(nums)):
            if exp != nums[i]:
                return exp
            
            exp += 1
        
        return len(nums)
