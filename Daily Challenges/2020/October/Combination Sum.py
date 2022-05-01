class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = defaultdict(list)
        for c in candidates:
            dp[c] = [[c]]
        
        for i in range(target + 1):
            for c in candidates:
                if i + c <= target:
                    for d in dp[i]:
                        
                        # check this to avoid duplicate
                        if c >= d[-1]:
                            dp[i + c].append(d + [c])
        
        return dp[target]
