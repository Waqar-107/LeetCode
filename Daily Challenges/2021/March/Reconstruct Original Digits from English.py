class Solution:
    def originalDigits(self, s: str) -> str:
        scnt = [0] * 26
        for ch in s:
            scnt[ord(ch) - ord('a')] += 1
        
        digits = ["zero", "two", "four", "six", "eight", "one", "five", "seven", "nine", "three"]
        digit_roman = [0, 2, 4, 6, 8, 1, 5, 7, 9, 3]
        dcnt = [0] * 10
        ans = []
        
        for idx, digit in enumerate(digits):
            cnt = [0] * 26
            for ch in digit:
                cnt[ord(ch) - ord('a')] += 1
            
            mn = 10**5
            for i in range(26):
                if cnt[i]:
                    mn = min(mn, scnt[i] // cnt[i])
            
            for i in range(26):
                if cnt[i]:
                    scnt[i] -= mn * cnt[i]
            
            while mn > 0:
                ans.append(str(digit_roman[idx]))
                mn -= 1
                
        ans.sort()
        return "".join(ans)
