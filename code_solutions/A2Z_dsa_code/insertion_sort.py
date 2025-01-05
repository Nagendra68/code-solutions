
class Solution:
    def __init__(self):
        pass
    def insertion_sort(self,arr):
        for i in range(1, len(arr)):  # Start from the second element
            key = arr[i] 
            j = i-1 # The element to insert
            while j>=0 and arr[j-1]>arr[j]:
                arr[j] = arr[j-1]
                j-=1
            arr[j] = key


              # Compare with elements in the sorted portion
                if arr[j - 1] > key:
                    arr[j] = arr[j - 1]  # Shift larger elements to the right
                else:
                    break  # Stop if no more shifting is needed
            arr[j] = key  # Insert the key
        return arr


arr = [5, 4, 2, 3, 1]
sol = Solution()
ans = sol.insertion_sort(arr)
print(arr)

