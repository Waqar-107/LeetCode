import itertools

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        combs = itertools.combinations(arr, k)
        
        ans = []
        for x in combs:
            if sum(x) == n:
                ans.append(list(x))
        
        return ans
