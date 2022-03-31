"""
1255. Maximum Score Words Formed by Letters

Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
"""


class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        import string
        from copy import deepcopy

        mapping = {}
        for i, letter in enumerate(string.ascii_lowercase):
            mapping[letter] = score[i]
        curMax = 0

        def dp(words, letters, curMax):
            cur_words = deepcopy(words)
            while words:
                word = words.pop()
                res, res_letters = compose(word, letters)
                if res:
                    curMax = max(dp(words, res_letters, curMax+res), dp(cur_words, letters, curMax))
                else:
                    curMax = dp(words, letters, curMax)
            return curMax

        def compose(word, letters):
            # returns score / None, remaining letters
            res = 0
            res_letters = deepcopy(letters)
            for letter in word:
                try:
                    idx = res_letters.index(letter)
                    del res_letters[idx]
                    res += mapping[letter]
                except:
                    return None, letters
            return res, res_letters

        curMax = dp(words, letters, curMax)
        return curMax

"""
Fail to pass some of the test cases
"""



############## Version. 2 ##############

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        import string
        from collections import Counter

        mapping = {}
        for i, letter in enumerate(string.ascii_lowercase):
            mapping[letter] = score[i]
        self.Max = 0
        cnt = Counter(letters)

        def dp(idx, cnt, curMax):
            if idx == len(words):
                self.Max = max(self.Max, curMax)
                return
            dp(idx + 1, cnt, curMax)
            cur = Counter(words[idx])
            if all(cur[k] <= cnt[k] for k in cur):
                cur_score = sum([mapping[lett] * cur[lett] for lett in cur])
                dp(idx + 1, cnt - cur, curMax + cur_score)

        dp(0, cnt, 0)
        return self.Max

"""
Runtime: 114 ms, faster than 89.39% of Python online submissions for Maximum Score Words Formed by Letters.
Memory Usage: 13.6 MB, less than 72.73% of Python online submissions for Maximum Score Words Formed by Letters.
"""

"""
Comments:
Instead of manipulating the given objects in-place such as by using del or pop(), keep them as-is and iterate through them with an index and dynamic argument.
"""