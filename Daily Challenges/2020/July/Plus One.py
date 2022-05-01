class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        digits = digits[::-1]
        
        for i in range(len(digits)):
            digits[i] += carry
            carry = digits[i] // 10
            q = digits[i] % 10
            digits[i] = q
        
        if carry:
            digits.append(1)
        
        return digits[::-1]
