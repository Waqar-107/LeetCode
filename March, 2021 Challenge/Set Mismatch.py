class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = [0] * n
        ans = [-1, -1]
        
        for i in range(n):
            cnt[nums[i] - 1] += 1
        
        for i in range(n):
            if cnt[i] == 2:
                ans[0] = i + 1
            elif cnt[i] == 0:
                ans[1] = i + 1
        
        return ans
