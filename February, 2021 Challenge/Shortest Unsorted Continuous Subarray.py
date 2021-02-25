class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = []
        n = len(nums)
        
        for e in nums:
            nums2.append(e)
            
        nums2.sort()

        first = n
        last = 0
        
        for i in range(n):
            if nums[i] != nums2[i]:
                first = min(first, i)
                last = max(last, i)
        
        return max(0, last - first + 1)
