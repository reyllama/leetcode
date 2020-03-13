'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

'''
Runtime: 5784 ms, faster than 16.73% of Python3 online submissions for Two Sum.
Memory Usage: 13.8 MB, less than 73.72% of Python3 online submissions for Two Sum.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mx = max(nums)
        mn = min(nums)
        for i in range(len(nums)):
            if nums[i] + mx < target | nums[i] + mn > target:
                continue
            for j in range(i+1, len(nums)):
                if nums[j] + mx < target | nums[j] + mn > target:
                    continue
                if nums[i] + nums[j] == target:
                    return [i,j]

'Time Limit Exceeded'

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = dict()
        for i, n in enumerate(nums):
            if n in memo:
                return [memo[n], i]
            memo[target-n] = i

'''
Runtime: 32 ms, faster than 99.96% of Python3 online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 53.72% of Python3 online submissions for Two Sum.
'''
