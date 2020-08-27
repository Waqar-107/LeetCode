class Solution:
    def ipv4(self, ip):
        for i in range(4):
            try:
                x = int(ip[i])
            except:
                return False
            
            if 0 <= x <= 255 and len(str(x)) == len(ip[i]) and 0 < len(ip[i]) <= 4:
                continue
            return False
        return True
    
    def ipv6(self, ip):
        ch = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']
        
        for i in range(8):
            if len(ip[i]) > 4 or len(ip[i]) < 1:
                return False
            
            for j in range(len(ip[i])):
                if ip[i][j] not in ch:
                    return False
        return True
        
        
    def validIPAddress(self, IP: str) -> str:
        arr = IP.split(".")
        arr2 = IP.split(":")
        
        if len(arr) == 4:
            if self.ipv4(arr):
                return "IPv4"
            else:
                return "Neither"
        elif len(arr2) == 8:
            if self.ipv6(arr2):
                return "IPv6"
            else:
                return "Neither"
        else:
            return "Neither"
        
