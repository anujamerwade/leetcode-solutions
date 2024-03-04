class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        maxScore = 0
        tokens.sort()
        
        while tokens:
            if tokens[0] <= power:
                # play it and increase score
                power -= tokens[0]
                score += 1
                maxScore = max(maxScore, score)
                tokens.remove(tokens[0])

            elif score >= 1:
                # play it reduce score
                maxToken = max(tokens)
                power += maxToken
                score -= 1
                tokens.remove(maxToken)
            else:
                break
        return maxScore
        