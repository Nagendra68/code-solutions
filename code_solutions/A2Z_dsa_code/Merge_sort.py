class Solution:
    def merge_sort(self, arr):
        # Base case: If the array has 1 or no elements, it's already sorted.
        if len(arr) <= 1:
            return arr
        
        # Find the middle index to divide the array
        mid = len(arr) // 2
        # Recursively sort both halves
        l_half = self.merge_sort(arr[:mid])
        r_half = self.merge_sort(arr[mid:])
        
        # Merge the sorted halves
        return self.merge(l_half, r_half)

    def merge(self, left, right):
        new = []  # List to store the merged elements
        i, j = 0, 0
        
        # Compare elements from both halves and merge them in sorted order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                new.append(left[i])
                i += 1
            else:
                new.append(right[j])
                j += 1
        
        # Add any remaining elements from the left or right half
        new.extend(left[i:])
        new.extend(right[j:])
        
        return new

# Example usage
arr = [4, 8, 5, 2, 6, 1, 66, 22, 35]
sol = Solution()
ans = sol.merge_sort(arr)
print(ans)

    
