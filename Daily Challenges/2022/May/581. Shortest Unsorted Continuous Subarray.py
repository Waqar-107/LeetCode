class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_list = copy.deepcopy(nums)
        sorted_list.sort()

        l = -1
        r = -1

        for i in range(len(sorted_list)):
            if nums[i] != sorted_list[i]:
                l = i
                break

        for i in range(len(sorted_list) - 1, -1, -1):
            if nums[i] != sorted_list[i]:
                r = i
                break

        if l != -1:
            return r - l + 1
        
        return 0
