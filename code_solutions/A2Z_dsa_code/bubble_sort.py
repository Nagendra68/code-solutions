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

# class Solution:
#     def bubble_sort1(self, arr):
#         for i in range(len(arr)-1):
#             swapped = False
#             for j in range(len(arr)-i-1):
#                 if arr[j]>arr[j+1]:
#                     arr[j],arr[j+1] = arr[j+1], arr[j]
#                     swapped = True
#             if swapped == False:
#                 return arr
#         return arr


class Solution:
    def bubbleSort(self, arr, n = None ):
        
        if n is None:
            n = len(arr)
        if n == 1:
            return arr
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        
        return self.bubbleSort(arr, n-1)
    

array = [64, 34, 25, 12, 22, 11, 90]
sol = Solution()

sorted_array = sol.bubble_sort1(array)
print("Sorted array:", sorted_array)

'''### **Bubble Sort - Complete Notes**

Bubble Sort is one of the simplest sorting algorithms. It repeatedly compares adjacent elements in a list and swaps them if they are in the wrong order. This process continues until the list is sorted.

---

### **Steps of Bubble Sort**

1. Start from the beginning of the list.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, **swap** them.
4. Move to the next pair of elements and repeat until the end of the list.
5. Repeat the entire process for the remaining unsorted elements until no swaps are needed.

---

### **Key Points**

- **Stable**: Maintains the relative order of equal elements.
- **In-Place**: No extra memory is used.
- **Time Complexity**:
    - **Best Case**:  (Already sorted)
        
        O(n)O(n)
        
    - **Worst Case**:  (Reversed order)
        
        O(n2)O(n^2)
        
    - **Average Case**:
        
        O(n2)O(n^2)
        
- **Space Complexity**:  (In-place sorting)
    
    O(1)O(1)'''