# Examples
# Input
# 4 7
# Output
# 2
# Input
# 4 9
# Output
# 3
# Input
# 1 1
# Output
# 1

class Solution:
    def Bear(self, s):
        cnt = 0
        while(s[0]<=s[1]):
            cnt+=1
            s[0] = s[0]*3
            s[1] = s[1]*2
        return cnt

s = list(map(int,input().split()))
sol = Solution()
ans = sol.Bear(s)
print(ans)

