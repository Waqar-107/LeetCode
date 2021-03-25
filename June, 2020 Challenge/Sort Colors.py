class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt = [0] * 3
        
        for n in nums:
            cnt[n] += 1
        
        idx = 0
        
        for i in range(3):
            while cnt[i]:
                nums[idx] = i
                idx += 1
                cnt[i] -= 1
        
