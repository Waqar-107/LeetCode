class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        req = 1
        
        while candies > 0:
            for i in range(num_people):
                ans[i] += min(req, candies)
                candies -= min(req, candies)
                req += 1
                
        return ans
