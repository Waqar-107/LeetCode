class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        expected = 1
        for n in arr:
            if n == expected:
                expected += 1
            else:
                if n - expected < k:
                    k -= (n - expected)
                    expected = n + 1
                else:
                    return expected + k - 1
        
        return arr[-1] + k
