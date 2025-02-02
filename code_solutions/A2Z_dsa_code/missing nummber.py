class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # for i in range(n+1):
        #     if i not in nums:
        #         return i
    
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
        actual_sum = sum(nums)
        return expected_sum - actual_sum