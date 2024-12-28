class Solution:
    def helpfulMaths(self, statement):
        statement.sort()
        statement = '+'.join(statement)
        return statement


statement = input().split('+')
sol = Solution()
ans = sol.helpfulMaths(statement)
print(ans)