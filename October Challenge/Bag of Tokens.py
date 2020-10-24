class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        score = 0
        
        while len(tokens):
            if P >= tokens[0]:
                score += 1
                P -= tokens[0]
                tokens.pop(0)
            
            elif score > 0 and len(tokens) > 1:
                score -= 1
                P += tokens[-1]
                tokens.pop()
            else:
                break
        
        return score
