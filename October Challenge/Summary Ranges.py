class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        q = []
        n = len(nums)
        
        ans = []
        for i in range(n):
            if len(q) == 0:
                q.append(nums[i])
            else:
                if q[-1] + 1 == nums[i]:
                    q.append(nums[i])
                
                else:
                    if len(q) > 1:
                        ans.append("{}->{}".format(q[0], q[-1]))
                    else:
                        ans.append(str(q[0]))
                    
                    q = [nums[i]]
                    
        if len(q) > 1:
            ans.append("{}->{}".format(q[0], q[-1]))
        elif len(q) == 1:
            ans.append(str(q[0]))
            
        return ans
