class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        i = 0
        j = len(people) - 1
        ans = 0
        
        while i <= j:
            if i == j:
                ans += 1
                break
            
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            
            else:
                j -= 1
                
            ans += 1
        
        return ans
