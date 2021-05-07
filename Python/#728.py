"""
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            nums = [int(k) for k in str(i)]
            flag = 1
            for num in nums:
                if num == 0:
                    flag = 0
                    break
                elif i % num != 0:
                    flag = 0
                    break
            if flag == 1:
                ans.append(i)
        return ans


"""
Runtime: 60 ms, faster than 32.86% of Python3 online submissions for Self Dividing Numbers.
Memory Usage: 14.2 MB, less than 81.76% of Python3 online submissions for Self Dividing Numbers.
"""
