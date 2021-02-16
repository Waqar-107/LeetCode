class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = set()
        for i in range(n + 1):
            for j in range(n + 1):
                # i / j
                if j > 0 and 0 < i / j < 1:
                    g = math.gcd(i, j)
                    ans.add(str(i // g) + "/" + str(j // g))

        return list(ans)
