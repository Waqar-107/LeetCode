class Solution:
    def ipv4(self, ip):
        arr = ip.split(".")
        if len(arr) != 4:
            return False
        
        for num in arr:
            if len(num) == 0:
                return False
            
            for ch in num:
                if not ('0' <= ch <= '9'):
                    return False
                
            if 0 <= int(num) <= 255 and len(str(int(num))) == len(num):
                continue
            
            return False
        
        return True
    
    def ipv6(self, ip):
        arr = ip.split(":")
        if len(arr) != 8:
            return False
        
        for num in arr:
            if len(num) < 1 or len(num) > 4:
                return False
            
            for ch in num:
                if '0' <= ch <= '9' or 'a' <= ch <= 'f' or 'A' <= ch <= 'F':
                    continue
                
                return False
        
        return True
        
    def validIPAddress(self, IP: str) -> str:
        if self.ipv4(IP):
            return "IPv4"
        
        elif self.ipv6(IP):
            return "IPv6"
        
        return "Neither"
        
