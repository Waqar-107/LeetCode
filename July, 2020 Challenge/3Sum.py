class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
            
        ans = set()
        
        n = len(nums)
        for i in range(n):
            cnt[nums[i]] -= 1
            
            for j in range(i + 1, n):
                cnt[nums[j]] -= 1
                
                t = -(nums[i] + nums[j])
                if t >= 0 and cnt[t] > 0:
                    lst = [nums[i], nums[j], t]
                    lst.sort()
                    ans.add(tuple(lst))
                
                cnt[nums[j]] += 1
            
            cnt[nums[i]] += 1
        
        ret = []
        for tup in ans:
            ret.append([tup[0], tup[1], tup[2]])
            
        return ret
            
