class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 1:
            return n
        
        up = [0] * n
        down = [0] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
        
        return 1 + max(down[n - 1], up[n - 1])
