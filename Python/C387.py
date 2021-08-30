"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        from string import ascii_lowercase
        
        d = defaultdict(list)
        ans = -1
        
        for i, letter in enumerate(s):
            d[letter].append(i)
            
        for letter in ascii_lowercase:
            if len(d[letter])==1:
                ans = min(ans, d[letter][0]) if ans>=0 else d[letter][0]
                
        return ans

"""
Runtime: 107 ms, faster than 85.42% of Python online submissions for First Unique Character in a String.
Memory Usage: 15.2 MB, less than 5.21% of Python online submissions for First Unique Character in a String.
"""