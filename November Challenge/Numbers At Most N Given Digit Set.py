class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        l = len(n)
        
        p = len(digits)
        cnt = 0
        
        # all numbers that has digits less than n
        for i in range(1, l):
            cnt += p
            p *= len(digits)
        
        dp = [0] * l + [1]
        for i in range(l - 1, -1, -1):
            for d in digits:
                if d < n[i]:
                    dp[i] += len(digits) ** (l - i - 1)
                elif d == n[i]:
                    dp[i] += dp[i + 1]
        
        return cnt + dp[0]
        
        
