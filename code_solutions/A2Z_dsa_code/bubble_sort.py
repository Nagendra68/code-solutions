# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):  # Number of passes
#         swapped = False
#         for j in range(n - i - 1):  # Compare pairs
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
#                 swapped = True
#         if not swapped:  # If no swaps, list is sorted
#             break
#     return arr

# # Example Usage
# array = [64, 34, 25, 12, 22, 11, 90]
# sorted_array = bubble_sort(array)
# print("Sorted array:", sorted_array)

class Solution:
    def bubble_sort1(self, arr):
        for i in range(len(arr)-1):
            swapped = False
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if swapped == False:
                return arr
        return arr

array = [64, 34, 25, 12, 22, 11, 90]
sol = Solution()

sorted_array = sol.bubble_sort1(array)
print("Sorted array:", sorted_array)