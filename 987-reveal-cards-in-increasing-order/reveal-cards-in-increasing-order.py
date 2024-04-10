class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [0]*n
        skip = False
        indexInDeck, indexInResult = 0, 0

        deck.sort()

        while indexInDeck < n:
            if result[indexInResult] == 0:
                if not skip:
                    # add element
                    result[indexInResult] = deck[indexInDeck]
                    indexInDeck += 1
                # else the curr position is skipped
                skip = not skip
            indexInResult = (indexInResult+1)%n
        return result