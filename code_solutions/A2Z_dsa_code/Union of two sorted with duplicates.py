class Solution:
    
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        c = []
        i, j = 0, 0
        
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                if len(c) == 0 or c[-1] != a[i]:  # Avoid duplicates
                    c.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if len(c) == 0 or c[-1] != b[j]:  # Avoid duplicates
                    c.append(b[j])
                j += 1
            else:  # a[i] == b[j]
                if len(c) == 0 or c[-1] != a[i]:  # Avoid duplicates
                    c.append(a[i])
                i += 1
                j += 1
        
        # Add remaining elements from a[] and b[] while avoiding duplicates
        while i < len(a):
            if len(c) == 0 or c[-1] != a[i]:
                c.append(a[i])
            i += 1
        
        while j < len(b):
            if len(c) == 0 or c[-1] != b[j]:
                c.append(b[j])
            j += 1

        return c