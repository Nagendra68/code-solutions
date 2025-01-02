#  1,11,111,1111,2,22
class Solution:
    def __init__(self):
        pass
    
    def BoringApartment(self,n ):
        ans = []
        for _ in range(n):
            num = input()
            s = int(num[0]) 
            length = len(num) 
            total = 10 * (s-1) 
            total += (length*(length+1))//2
            ans.append(total) 
        return ans


n = int(input())
sol = Solution()
ans = sol.BoringApartment(n)
for num in ans:
    print(num)



