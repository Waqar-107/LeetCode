class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        i = 0
        idx = 0
        while i < n:
            j = i + 1
            cnt = 1
            val = nums[i]
            nums[idx] = val
            idx += 1
            
            while j < n:
                if nums[j] == val:
                    cnt += 1
                    j += 1
                    
                    if cnt <= 2:
                        nums[idx] = val
                        idx += 1
                    
                else:
                    break
            
            
            ans += min(2, cnt)
            i = j
        
        return ans
