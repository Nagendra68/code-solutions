class Solution:
    def reverseArray(self, arr):
        # code here
        
        # using for loop
        # n = len(arr)
        # for i in range(len(arr)//2):
        #     arr[i],arr[n-i-1] = arr[n-i-1], arr[i]

        # return arr
        
        # using Recursion
        # Base Case: When the array length is 0 or 1, it is already reversed
        if len(arr) <= 1:
            return arr

        # Swap the first and last elements
        arr[0], arr[-1] = arr[-1], arr[0]

        # Recursive call on the subarray excluding the first and last elements
        # Pass only the middle part for recursion
        arr[1:-1] = self.reverseArray(arr[1:-1])

        return arr