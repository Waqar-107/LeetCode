class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = {}
        for e in nums:
            if e in cnt:
                cnt[e] += 1
            else:
                cnt[e] = 1
        
        ans = 0
        for key in cnt:
            if key == k - key:
                ans += cnt[key]
            else:
                if (k - key) in cnt:
                    ans += min(cnt[key], cnt[k - key])
        
        return ans // 2
