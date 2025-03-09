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