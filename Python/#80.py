"""
80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.
"""

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

"""
Runtime: 46 ms, faster than 70.36% of Python online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 13.5 MB, less than 56.05% of Python online submissions for Remove Duplicates from Sorted Array II.
"""
