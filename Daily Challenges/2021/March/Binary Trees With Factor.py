class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        
        arr.sort()
        dp = [1] * n
        
        index = {}
        for i in range(n):
            index[arr[i]] = i
        
        for i in range(n):
            for j in range(i):
                # arr[j] is less than arr[i], so it will be a left child
                if arr[i] % arr[j] == 0:
                    right = arr[i] // arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= mod
        
        return sum(dp) % mod
                
