# class Solution:
#     def selection_sort(self, arr):
#         n = len(arr)

#         for i in range(n-1):
#             min_index = i
#             for j in range(i+1, n):
#                 if arr[j]<arr[min_index]:
#                     min_index = j
#             arr[i], arr[min_index] = arr[min_index], arr[i]
#         return arr


# arr = [64, 34, 25, 12, 22, 11, 90]
# sol = Solution()
# sorted_arr = sol.selection_sort(arr)
# print("Sorted Array:", sorted_arr)

class Solution:
    def selection_sort1(self,arr):
        for i in range(len(arr)-1):
            min_index = i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_index]:
                    min_index = j
            arr[i],arr[min_index] = arr[min_index], arr[i]
        return arr

arr = [64, 34, 25, 12, 22, 11, 90]
sol = Solution()
sorted_arr = sol.selection_sort1(arr)
print("Sorted Array:", sorted_arr )

'''In-depth Notes: Selection Sort
Concept:
Selection Sort is a simple comparison-based sorting algorithm. It repeatedly selects the smallest (or largest) element from the unsorted part of the list and moves it to the sorted part. It is an in-place, unstable sorting algorithm.
Algorithm Steps:
Start with the first element (index 0).
Find the smallest element in the unsorted portion of the array.
Swap it with the first element of the unsorted portion.
Move the boundary between sorted and unsorted portions by one position.
Repeat until the entire array is sorted.
Key Characteristics:
Time Complexity:
Best, Worst, and Average Case:  because of the nested loops.
O(n2)O(n^2)
Space Complexity:  (in-place sort; no extra memory needed).
O(1)O(1)
Unstable Algorithm: Does not maintain the relative order of equal elements.'''