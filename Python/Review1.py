class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.ans = []

        def helper(target, nums, arr):
            if target < 0:
                return
            if target==0:
                self.ans.append(arr)
            else:
                for i in range(len(nums)):
                    helper(target-nums[i], nums[i:], arr+[nums[i]])

        return self.ans