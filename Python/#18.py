"""
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums, res = sorted(nums), set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                if nums[i]>=0 and nums[j]>=0 and nums[i]+nums[j]>target:
                    break
                x, y = j+1, len(nums)-1
                while y>x:
                    if nums[i]+nums[j]+nums[x]+nums[y]==target:
                        res.add((nums[i], nums[j], nums[x], nums[y]))
                        x += 1
                        y -= 1
                    elif nums[i]+nums[j]+nums[x]+nums[y] < target:
                        x += 1
                    else:
                        y -= 1
        return [arg for arg in res]

"""
Runtime: 1812 ms, faster than 10.34% of Python3 online submissions for 4Sum.
Memory Usage: 14.1 MB, less than 7.14% of Python3 online submissions for 4Sum.
"""

class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		l = len(nums)
		d = {}
		res = set()
		nums.sort()
		for i in range(l - 1):
			for j in range(i + 1, l):
				key = nums[i] + nums[j]
				if key not in d:
					d[key] = [(i, j)]
				else:
					d[key].append((i, j))
		for i in range(2, l - 1):
			for j in range(i + 1, l):
				pre = target - nums[i] - nums[j]
				if pre in d:
					for v in d[pre]:
						if v[1] < i:
							res.add((nums[v[0]], nums[v[1]], nums[i], nums[j]))
		return [list(i) for i in res]

"""
Runtime: 124 ms, faster than 78.90% of Python3 online submissions for 4Sum.
Memory Usage: 17.6 MB, less than 7.14% of Python3 online submissions for 4Sum.
"""
