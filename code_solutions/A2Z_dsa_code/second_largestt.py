class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
        
        max_val = sec_max = float('-inf')
        
        for num in arr:
            if num > max_val:
                sec_max = max_val
                max_val = num
            elif num > sec_max and num != max_val:
                sec_max = num
        
        return sec_max if sec_max != float('-inf') else -1