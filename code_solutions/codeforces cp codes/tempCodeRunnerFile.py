class Solution:
    def Arrival_of_the_general(self, n):
        num = list(map(int,input().split()))
        big = float('-inf')
        small = float('inf')
        small_i = big_i = 0
        for i in range(n):
            if num[i]>big:
                big = num[i]
                big_i = i
            if num[i]<=small:
                small = num[i]
                small_i = i
        return (big_i) + (n-small_i-1)  

n = int(input())
sol = Solution()
result = sol.Arrival_of_the_general(n)