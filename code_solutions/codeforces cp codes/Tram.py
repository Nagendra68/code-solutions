'''Input
4
0 3   left join 
2 5
4 2
4 0
Output
6'''

class Solution:
    def Tram(self, n):
        cnt = 0
        max_cnt = 0
        for _ in range(n):
            drive = list(map(int,input().split()))
            if cnt!=0:
                cnt = cnt - drive[0]

            cnt = cnt + drive[1]

            if cnt> max_cnt:
                max_cnt = cnt

        return max_cnt

n = int(input())
sol = Solution()
ans = sol.Tram(n)
print(ans)






