class Solution:
    def maxRepOpt1(self, text: str) -> int:
        mp = defaultdict(list)
        
        i = 0
        while i < len(text):
            j = i + 1
            length = 1
            
            while j < len(text):
                if text[i] == text[j]:
                    length += 1
                    j += 1
                else:
                    break
                    
            mp[text[i]].append((i, length))
            i += length
        
        ans = 0
        for c in range(26):
            ch = chr(97 + c)
            
            if len(mp[ch]) == 0:
                continue
                
            ans = max(ans, mp[ch][0][1])
            for i in range(1, len(mp[ch]), 1):
                # check if the middle parts length is 1
                if mp[ch][i][0] - (mp[ch][i - 1][0] + mp[ch][i - 1][1]) == 1:
                    if len(mp[ch]) > 2:
                        ans = max(ans, mp[ch][i - 1][1] + mp[ch][i][1] + 1)
                    else:
                        ans = max(ans, mp[ch][i - 1][1] + mp[ch][i][1])
                else:
                    ans = max(ans, mp[ch][i - 1][1] + 1, mp[ch][i][1] + 1)
        
        return ans
           
