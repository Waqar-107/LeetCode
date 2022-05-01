class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        left = [False] * n
        
        mn = math.inf
        for i in range(n):
            if mn < nums[i]:
                left[i] = True
            
            mn = min(nums[i], mn)
        
        mx = -math.inf
        for i in range(n - 1, -1, -1):
            if mx > nums[i] and left[i]:
                return True
            
            mx = max(mx, nums[i])
        
        return False
