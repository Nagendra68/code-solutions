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

'''### Short Notes: Insertion Sort

**Definition**:

Insertion Sort is a simple sorting algorithm that builds the final sorted array one element at a time by comparing and inserting elements into their correct position.

---

**Steps**:

1. Start with the second element (index 1) in the array.
2. Compare it with elements before it.
3. If it's smaller, move the previous elements one step ahead and insert the current element into its correct position.
4. Repeat this for each element in the array until the whole array is sorted.

---

**Example**:
Input: `[5, 3, 4, 1]`

- Step 1: Compare `3` with `5`, insert before `5` → `[3, 5, 4, 1]`
- Step 2: Compare `4`, insert before `5` → `[3, 4, 5, 1]`
- Step 3: Compare `1`, insert at the start → `[1, 3, 4, 5]`
Output: `[1, 3, 4, 5]`

---

**Algorithm (Pseudocode)**:

1. Loop from index 1 to the end of the array.
2. Pick the current element.
3. Shift elements of the sorted portion (left side) if they are larger than the current element.
4. Insert the current element at the correct position.'''

