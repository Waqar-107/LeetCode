class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        rem = sum(nums) - x
        
        if rem < 0: 
            return -1
        
        longest_rem = -1
        left = 0
        
        for right in range(n):
            rem -= nums[right]
            while rem < 0:
                rem += nums[left]
                left += 1
                
            if rem == 0:
                longest_rem = max(longest_rem, right - left + 1)
            
        
        if longest_rem == -1:
            return -1
        
        return n - longest_rem
        
