class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = defaultdict(list)
        
        for i in range(len(nums)):
            mp[nums[i]].append(i + 1)
        
        for key in mp:
            for i in range(len(mp[key])):
                j = bisect.bisect_right(mp[key], mp[key][i] + k)
                
                if j > i + 1:
                    return True
        return False
