
class Solution(object):
    def maxProduct(self, nums):

        if not nums:
            return 0
        
        max_prod = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            temp_max = max(curr, curr*max_so_far, curr*min_so_far)
            min_so_far = min(curr, curr*max_so_far, curr*min_so_far)
            max_so_far = temp_max

            max_prod = max(max_prod, max_so_far)

        return max_prod