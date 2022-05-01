class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        
        while len(b) < 32:
            b = '0' + b
        
        b = b[::-1]
        return int(b, 2)
