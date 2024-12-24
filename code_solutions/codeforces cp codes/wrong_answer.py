'''Input
512 4
Output
50
Input
1000000000 9
Output
1'''

class Solution:
    def wrong_answer(self, stat):
        for _ in range(statement[1]):
            if statement[0]%10 != 0:
                statement[0]-=1
            else:
                statement[0]/=10

        print(int(statement[0]))

statement = list(map(int, input().split()))
sol = Solution()
sol.wrong_answer(statement)
