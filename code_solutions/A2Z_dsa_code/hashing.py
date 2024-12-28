
# arr[] = [2, 3, 2, 3, 5]
# Output: [0, 2, 2, 0, 1]
# Example

class Solution:
    def count_frequency(self, arr):
        n = len(arr)  # Length of the array is the size of the range 1 to n
        result = [0] * n  # Initialize result array with 0s
        
        # Count the frequency of each element in arr
        for num in arr:
            result[num - 1] += 1
        
        return result


arr = [2, 3, 2, 3, 5]
sol = Solution()
ans = sol.count_frequency(arr)
print(ans)

