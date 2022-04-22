"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.res = []
        
	# avoid in-place ops 
        def dp(idx=0, cur=[]):
            if idx == len(s):
                self.res.append(cur)
            for j in range(1, len(s)-idx+1):
                if is_palindrome(s[idx:idx+j]):
                    dp(idx+j, cur+[s[idx:idx+j]])

	# should cover len(string)==1 case
        def is_palindrome(string):
            if len(string)==1:
                return True
            half = len(string) // 2
            res = True
            for i in range(half):
                if string[i] != string[-i-1]:
                    res = False
            return res
        
        dp()
        
        return self.res

"""
Runtime: 684 ms, faster than 89.20% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.1 MB, less than 70.39% of Python3 online submissions for Palindrome Partitioning.
"""
