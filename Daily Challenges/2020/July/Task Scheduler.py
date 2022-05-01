class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        length = len(tasks)

        for ch in tasks:
            cnt[ord(ch) - ord('A')] += 1
            
        cnt.sort()
        
        mx = cnt.pop()
        idle = (mx - 1) * n
        
        while len(cnt) and idle > 0:
            idle -= min(mx - 1, cnt.pop())
            idle = max(0, idle)
        
        return idle + len(tasks)
        
        
