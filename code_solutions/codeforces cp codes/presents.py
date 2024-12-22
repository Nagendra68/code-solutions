'''i/p ->  
4  quantity of friends Petya invited to the party
1 2 3 4
2 3 4 1 pi — the number of a friend who gave a gift to friend number i.
o/p ->
4 1 2 3 Print n space-separated integers:
        the i-th number should equal the number of the friend who gave a gift to friend number i.
'''

class Solution:
    def presents(self, n):
        num = list(map(int, input().strip().split()))
        dictt = {}
        for i in range(1, n+1):
            dictt[i] = num[i-1]
        swapped_dict = {v:k for k, v in dictt.items()}
        sorted_dictt = {k:swapped_dict[k] for k in sorted(swapped_dict)}
        new = list(sorted_dictt.values())
        new2 = " ".join(map(str, new))
        
        return new2

n = int(input())
sol = Solution()
ans = sol.presents(n)
print(ans)


# dictt = {6:1, 1:2}
# print(dictt.items())
# print(dictt)
# print(sorted(dictt))
# sorted_dict = {k: dictt[k] for k in sorted(dictt)}
# print(sorted_dict)