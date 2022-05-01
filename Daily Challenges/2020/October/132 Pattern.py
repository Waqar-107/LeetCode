class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minSoFar = nums[0]
        
        for i in range(1, len(nums), 1):
            if nums[i] <= minSoFar:
                minSoFar = nums[i]
            else:
                for j in range(i + 1, len(nums), 1):
                    if nums[i] > nums[j] > minSoFar:
                        return True
        
        return False
