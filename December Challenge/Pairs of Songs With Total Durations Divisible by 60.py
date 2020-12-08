class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = defaultdict(int)
        
        for i in range(len(time)):
            time[i] %= 60
            cnt[time[i]] += 1
            
        ans = 0
        for i in range(len(time)):
            if time[i] == 0:
                ans += cnt[0] - 1
            elif 60 - time[i] == time[i]:
                ans += cnt[time[i]] - 1
            else:
                ans += cnt[60 - time[i]]
        
        return ans // 2
