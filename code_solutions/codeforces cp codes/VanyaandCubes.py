class Solution:
    def __init__(self):
        pass

    def total_row(self, n):
        total = 0
        height = 0
        for i in range(1,n+1):
            column = i*(i+1)/2
            total = total + column
            if total>n:
                return height
            height+=1
        return height
            
n = int(input())           
sol = Solution()
ans = sol.total_row(n)
print(ans)
        
