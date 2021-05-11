"""
950. Reveal Cards In Increasing Order

In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.
"""

class Solution:
    def deckRevealedIncreasing(self, deck):

        out = [0] * len(deck)
        self.order = []
        self.arr = list(range(len(deck)))

        def getOrder(subdeck):

            if len(subdeck) % 2 == 1:
                is_odd = True
            else:
                is_odd = False

            if len(subdeck) <= 2: # End case
                self.order += subdeck
                return

            for i, v in enumerate(subdeck[:-1]):

                if i % 2 == 0: # Those that are taken out right away
                    self.order.append(v)
                    self.arr.remove(v)

            if is_odd: # Last entry was kept untouched
                self.arr = [self.arr[-1]] + self.arr[:-1]
            getOrder(self.arr)

        getOrder(self.arr)
        sor_deck = sorted(deck)

        for i in range(len(deck)):
            out[self.order[i]] = sor_deck[i]

        return out

"""
Runtime: 52 ms, faster than 28.48% of Python3 online submissions for Reveal Cards In Increasing Order.
Memory Usage: 14.7 MB, less than 5.83% of Python3 online submissions for Reveal Cards In Increasing Order.
"""
