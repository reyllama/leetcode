"""
338. Counting Bits


Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        temp = [0]
        if num <= len(temp)-1:
            return temp[:num+1]
        else:
            for i in range(len(temp), num+1):
                temp.append('{0:08b}'.format(i).count('1'))
            return temp

"""
Runtime: 152 ms, faster than 14.44% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 54.31% of Python3 online submissions for Counting Bits.
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        return ['{0:08b}'.format(i).count('1') for i in range(num+1)]

"""
Runtime: 156 ms, faster than 13.67% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 7.47% of Python3 online submissions for Counting Bits.
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num+1):
            res.append(res[i//2]+(i%2))
        return res
