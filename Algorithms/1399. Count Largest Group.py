class Solution:
    def digit_sum(self, n):
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        
        return ans
    
    def countLargestGroup(self, n: int) -> int:
        mx = 0
        freq = defaultdict(int)
        
        for i in range(1, n + 1):
            x = self.digit_sum(i)
            freq[x] += 1
            mx = max(mx, freq[x])
        
        ans = 0
        for key in freq:
            if freq[key] == mx:
                ans += 1
        
        return ans
