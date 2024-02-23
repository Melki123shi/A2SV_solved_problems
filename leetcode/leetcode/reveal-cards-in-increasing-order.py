class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) < 3:
            return deck

        deck.sort()

        reveal_order = deque([deck[-1]])
        for i in range(len(deck) - 2, -1, -1):
            val = reveal_order.popleft()
            reveal_order.append(val)
            reveal_order.append(deck[i])

        reveal_order = list(reveal_order)[::-1]
        return reveal_order


