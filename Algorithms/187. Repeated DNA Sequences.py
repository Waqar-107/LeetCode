# from dust i have come, dust i will be

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = {}
        
        for i in range(len(s) - 10 + 1):
            t = s[i : i + 10]
            # print(t)
            if t in mp:
                mp[t] += 1
            else:
                mp[t] = 1
        
        ret = []
        for t in mp:
            if mp[t] > 1:
                ret.append(t)
        
        return ret
