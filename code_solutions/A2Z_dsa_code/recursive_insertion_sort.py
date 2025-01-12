class Solution:
    def insertionSort(self, arr, n=None):
        # Initialize n as the length of the array on the first call
        if n is None:
            n = len(arr)
        
        # Base case: If the array has 1 or fewer elements, it's already sorted
        if n <= 1:
            return
        
        # Recursively sort the first n-1 elements
        self.insertionSort(arr, n - 1)
        
        # Insert the nth element into the sorted part
        key = arr[n - 1]
        j = n - 2
        
        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key