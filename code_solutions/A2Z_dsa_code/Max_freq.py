class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()  # Sort the array
        left = 0
        total = 0
        max_freq = 0

        for right in range(len(nums)):
            total += nums[right]  # Add the current element to total
            
            # Check if the current window is valid
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]  # Shrink the window
                left += 1

            # Update the maximum frequency
            max_freq = max(max_freq, right - left + 1)

        return max_freq
