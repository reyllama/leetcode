"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp = str(int(a)+int(b))
        for i in range(1, len(temp[::-1])+1):
            if int(temp[-i])>1:
                if i == 1:
                    temp = temp[:-i-1] + str(int(temp[-i-1])+1) + str(int(temp[-i])-2)
                elif i == len(temp):
                    temp = '1' + str(int(temp[-i])-2) + temp[-i+1:]
                else:
                    temp = temp[:-i-1] + str(int(temp[-i-1])+1) + str(int(temp[-i])-2) + temp[-i+1:]
        return temp

case = Solution()
print(case.addBinary('101', '11'))
