class Solution:
    def getSecondLargest(self, arr):
        unique_arr = list(set(arr))
        if len(unique_arr)<2:
            return -1
        first = unique_arr[0]
        second = unique_arr[1]
        if first<second:
            second, first = first, second
        for i in range(2, len(unique_arr)):
            if unique_arr[i]>second:
                if unique_arr[i]>first:
                    second = first
                    first = unique_arr[i]
                else:
                    second = unique_arr[i]
        return second