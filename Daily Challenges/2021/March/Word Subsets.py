class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        n = len(A)
        m = len(B)
        
        cntB = [0] * 26
        for i in range(m):
            cnt = [0] * 26
            for ch in B[i]:
                cnt[ord(ch) - ord('a')] += 1
            
            for j in range(26):
                cntB[j] = max(cntB[j], cnt[j])
        
        ans = []
        for word in A:
            cnt = [0] * 26
            for ch in word:
                cnt[ord(ch) - ord('a')] += 1
            
            flag = True
            for j in range(26):
                if cnt[j] < cntB[j]:
                    flag = False
                    break
                
            if flag:
                ans.append(word)
        
        return ans
            
