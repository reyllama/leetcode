class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pprev, prev = None, None
        k = len(nums)
        i = 0
        
        while i < k:
            if pprev is None:
                pprev = nums[i]
                i += 1
                continue
            elif prev is None:
                prev = nums[i]
                i += 1
                continue
            else:
                if prev==pprev and prev==nums[i]:
                    del nums[i]
                    k -= 1
                else:
                    pprev = prev
                    prev = nums[i]
                    i += 1
        return k

