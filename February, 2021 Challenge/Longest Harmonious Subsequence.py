class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        
        for number in nums:
            cnt[number] += 1
        
        for number in nums:
            if number + 1 in cnt:
                ans = max(ans, cnt[number] + cnt[number + 1])
        
        return ans
        
