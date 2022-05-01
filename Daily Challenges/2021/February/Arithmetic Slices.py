class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        cnt = 1
        
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                ans += cnt
                cnt += 1
            else:
                cnt = 1
        
        return ans
