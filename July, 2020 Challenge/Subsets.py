from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        ans = [[]]
        for i in range(1, n + 1):
            comb = combinations(nums, i)
        
            for tup in comb:
                ans.append(list(tup))
                
        return ans
