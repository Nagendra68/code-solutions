'''i/p ->n = 4
o/p -> sum of divisors from 1 to n
        i.e f(1) = 1
            f(2) = 1+2 = 3
            f(3) = 1 + 3 = 4
            f(4) = 1 + 2 +4 = 7
            result = 1 + 3 + 4 + 7 = 15
            
            '''
class Solution:
    def sumOfDivisors(self, n):
        sums = [0]*(n+1)
        for i in range(1, n+1):
            for j in range(i, n+1, i):
                sums[j]+=i
        return sum(sums[1:])




n = int(input())
sol = Solution()
answer = sol.sumOfDivisors(n)
print(answer)