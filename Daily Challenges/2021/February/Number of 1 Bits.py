class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(32):
            if (1 << i) & n:
                cnt += 1
        
        return cnt
