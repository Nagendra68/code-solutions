# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]  # Element to be inserted
#         j = i - 1
#         # Shift elements of the sorted part to the right
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key  # Insert the key at the correct position
#     return arr

# # Example Usage
# arr = [5, 3, 8, 6, 2]
# sorted_arr = insertion_sort(arr)
# print("Sorted Array:", sorted_arr)
# Output:

def insertion_sort2(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

arr = [5, 3, 8, 6, 2]
sorted_arr = insertion_sort2(arr)
print("Sorted Array:", sorted_arr)


