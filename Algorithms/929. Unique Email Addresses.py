# from dust i have come, dust i will be

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails = set()
        
        for m in emails:
            localName, domain = m.split('@')
            
            local = localName.split('+')
            actualLocal = local[0]
            
            arr = actualLocal.split(".")
            
            addr = "".join(arr) + '@' + domain
            print(addr)
            mails.add(addr)
        
        return len(mails)
