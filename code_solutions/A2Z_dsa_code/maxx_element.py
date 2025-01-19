
class Solution:
    def largest(self, arr):
        # code here
        n = len(arr)
        maxx = arr[0]
        for i in range(1,n):
            if arr[i]> maxx:
                maxx = arr[i]
        return maxx