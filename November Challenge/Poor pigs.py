class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(T))
