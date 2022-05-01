class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        cnt = [0] * 101
        
        for num in arr:
            cnt[num] += 1
        
        ans = 0
        
        # all are diff
        for x in range(101):
            for y in range(x + 1, 101):
                z = target - x - y
                
                if x < y < z <= 100:
                    ans += cnt[x] * cnt[y] * cnt[z]
                    ans %= mod

        # x == y
        for x in range(101):
            z = target - x - x
            if x < z <= 100:
                ans += (cnt[x] * (cnt[x] - 1)) // 2 * cnt[z]
                ans %= mod

        # y == z
        for x in range(101):
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                
                if x < y <= 100:
                    ans += (cnt[x] * cnt[y] * (cnt[y] - 1)) // 2
                    ans %= mod
        
        # x == y == z
        if target % 3 == 0:
            x = target // 3
            ans += (cnt[x] * (cnt[x] - 1) * (cnt[x] - 2)) // 6
            ans %= mod
        
        
        return ans
