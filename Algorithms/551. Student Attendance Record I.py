class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1
                late = 0
            
            elif s[i] == 'L':
                late += 1
            
            else:
                late = 0
            
            if late == 3:
                return False
        
        return absent <= 1
