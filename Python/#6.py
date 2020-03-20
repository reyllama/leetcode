'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows<2:
            return s
        import numpy as np
        i, dir, ind = 1, 0, dict()
        ind[0] = list(np.arange(0, len(s), 2*numRows-2))
        ind[numRows-1] = list(np.arange(numRows-1, len(s), 2*numRows-2))
        stops = ind[0][1:]+ind[numRows-1]
        for k in range(1, numRows-1):
            ind[k] = []
        while i<len(s):
            if i in stops:
                dir = 1-dir
                i += 1
                continue
            if dir==0:
                ind[i%(numRows-1)].append(i)
            elif dir==1:
                ind[numRows-1-(i%(numRows-1))].append(i)
            i += 1
        return "".join([s[i] for j in range(numRows) for i in ind[j]])

'''
Runtime: 192 ms, faster than 9.54% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 28.4 MB, less than 5.71% of Python3 online submissions for ZigZag Conversion.
'''

class Solution:
# @return a string
def convert(self, s, n):
    res = [[] for _ in range(n)]
    i = 0
    try:
        while True:
            for r in res:
                r.append(s[i])
                i += 1
            for r in res[-2:0:-1]:
                r.append(s[i])
                i += 1
    except IndexError:
        return ''.join(''.join(r) for r in res)

'''
Runtime: 56 ms, faster than 74.20% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 13.1 MB, less than 98.57% of Python3 online submissions for ZigZag Conversion.
'''
