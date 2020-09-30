"""
determine the first missing positive.

1. make all the negatives 0
2. shift all the 0 to the left
3. for all the numbers in the array try to make num[i] = i + 1; consider 0-indexing
   3.1. if 0 then nothing to do
   3.2. if duplicate then assign 0 to it. how to understand that it'd duplicate? if the actual index where the number should be already holds that                  number then it's a duplicate.
   3.3. while the number in i does not holds the number it should hold, try swapping num[i] with the index where it should be.
4. for all the index, select the first that does not hold the correct value.
"""

import math

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 1
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] >= (n + 1):
                nums[i] = 0
                
        # move the zeros to the left
        idx = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i] = nums[idx]
                nums[idx] = 0
                idx += 1
                
        # now place all the numbers according to their index
        for i in range(n):
            # zero
            if nums[i] == 0:
                continue
                
            # duplicate
            if nums[nums[i] - 1] == nums[i] and i + 1 != nums[i]:
                nums[i] = 0
                continue
                
            # change positions
            idx = i
            while nums[nums[idx] - 1] != nums[idx] and nums[idx]:
                # swap
                temp = nums[nums[idx] - 1]
                nums[nums[idx] - 1] = nums[idx]
                nums[idx] = temp

            
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
        
