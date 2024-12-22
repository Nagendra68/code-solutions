'''i/p->
40047
o/p->
NO
i/p->
7747774
o/p->
YES
'''
class Solution:
    def lucky_number(self, num):
        cnt = 0
        for digits in num:
            if digits in {'4', '7'}:
                cnt+=1
        # cnt = str(cnt)
        if cnt not in {4, 7}:
            return "NO"
        return "YES"

num = input().strip()
sol  = Solution()
answer = sol.lucky_number(num)
print(answer)
