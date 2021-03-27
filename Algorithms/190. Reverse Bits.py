class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        b = b[::-1]
        
        while len(b) < 32:
            b += "0"
        
        return int(b, 2)
