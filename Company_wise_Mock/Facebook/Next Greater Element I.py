class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = defaultdict(int)
        for i in range(len(nums2)):
            idx[nums2[i]] = i
        
        for i in range(len(nums1)):
            if nums1[i] not in idx:
                nums1[i] = -1
            else:
                ans = -1
                for j in range(idx[nums1[i]], len(nums2)):
                    if nums1[i] < nums2[j]:
                        ans = nums2[j]
                        break
                
                nums1[i] = ans
        
        return nums1
