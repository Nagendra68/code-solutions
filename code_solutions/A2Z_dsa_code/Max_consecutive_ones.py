class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cnt,cnt = 0,0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            else:
                max_cnt = max(cnt, max_cnt)
                cnt = 0
        max_cnt = max(cnt, max_cnt)

        return max_cnt