# i/p -> 
# 4
# 33 44 11 22
# o/p ->
# 2

# i/p -> 
# 7
# 10 10 58 31 63 40 76

# o/p ->
# 10

class Solution:
    def Arrival_of_the_general(self, n):
        num = list(map(int,input().strip().split()))
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
        total_moves = (big_i) + (n-small_i-1)
        if big_i > small_i:
            return (big_i) + (n - small_i - 1) - 1  # Subtract 1 for overlap
        else:
            return (big_i) + (n - small_i - 1)


n = int(input())
sol = Solution()
result = sol.Arrival_of_the_general(n)
print(result)



# 1, 2
# 1, 2
# 6, 1
# 6, 7-1-1
# 1, 4-2-1=1


