class Solution:
    def drink(self, n, k, l, c, d, p, nl, np):
        total_drink = k * l
        toast_from_drink = total_drink // nl
        toast_from_limes = c * d
        toast_from_salt = p // np
        return min(toast_from_drink, toast_from_limes, toast_from_salt) // n

data = list(map(int, input().split()))
solution = Solution()
answer = solution.drink(*data)
print(answer)
