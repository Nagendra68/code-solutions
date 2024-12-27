class Solution:
    def BoyOrGirl(self, name):
        if len(name)%2!=0:
            return "IGNORE HIM!"
        else:
            return "CHAT WITH HER!"



name = set(str(input()))
sol = Solution()
ans = sol.BoyOrGirl(name)
print(ans)

