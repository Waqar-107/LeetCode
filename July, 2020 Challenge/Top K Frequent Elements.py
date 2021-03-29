class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        
        for n in nums:
            cnt[n] += 1
        
        arr = []
        for key in cnt:
            arr.append((key, cnt[key]))
            
        arr.sort(key=lambda x: (-x[1], x[0]))
        
        ans = []
        for n in arr:
            ans.append(n[0])
            
        return ans[:k]
