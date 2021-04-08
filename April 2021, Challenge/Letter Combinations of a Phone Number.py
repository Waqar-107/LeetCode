class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        
        # first digit
        for ch in mapping[ord(digits[0]) - ord('0')]:
            ans.append(ch)
            
        for i in range(1, len(digits)):
            new_ans = []
            for ex in ans:
                for ch in mapping[ord(digits[i]) - ord('0')]:
                    new_ans.append(ex + ch)
            
            ans = []
            for element in new_ans:
                ans.append(element)
        
        return ans
