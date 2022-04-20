"""
1025. Divisor Game

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

    Choosing any x with 0 < x < n and n % x == 0.
    Replacing the number n on the chalkboard with n - x.

Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.
"""

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

"""
Runtime: 24 ms, faster than 98.78% of Python3 online submissions for Divisor Game.
Memory Usage: 14 MB, less than 21.04% of Python3 online submissions for Divisor Game.
"""
