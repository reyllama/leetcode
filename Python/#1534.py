"""
1534. Count Good Triplets

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

"""

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                if abs(arr[i]-arr[j]) <= a:
                    for k in range(j+1, n):
                        if abs(arr[j]-arr[k])<=b:
                            if abs(arr[i]-arr[k])<=c:
                                cnt += 1
        return cnt

"""
Runtime: 368 ms, faster than 89.43% of Python3 online submissions for Count Good Triplets.
Memory Usage: 14.4 MB, less than 41.41% of Python3 online submissions for Count Good Triplets.
"""
