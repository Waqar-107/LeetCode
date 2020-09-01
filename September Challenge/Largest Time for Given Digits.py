import itertools
import re

class Solution:
    def isValid(self, s):
        time_re = re.compile(r'^([01]\d|2[0-3]):([0-5]\d)$')
        return bool(time_re.match(s))
        
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = list(itertools.permutations(A))
        ret = ""
        
        for arr in ans:
            s = str(arr[0]) + str(arr[1]) + ":" + str(arr[2]) + str(arr[3])

            # if valid then check if max
            if self.isValid(s):
                if ret == "" or ret < s:
                    ret = s
        return ret
        
