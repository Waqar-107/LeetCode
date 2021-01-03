class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        arr = permutations(nums)
        
        ans = set()
        for p in arr:                
            ans.add(p)
            
        ret = []
        for p in ans:
            ret.append([])
            for i in range(len(p)):
                ret[-1].append(p[i])
        
        return ret
