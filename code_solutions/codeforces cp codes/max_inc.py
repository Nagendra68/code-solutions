# Input
# 5
# 1 7 2 11 15
# Output
# 3
# Input
# 6
# 100 100 100 100 100 100
# Output
# 1
# Input
# 3
# 1 2 3
# Output
# 3

class Solution:
    def __init__(self):
        pass

    def max_inc(self, n):
        arr = list(map(int, input().split()))
        cnt = max_cnt = 1  # Start with the minimum subsequence length
        i = 1

        while i < n:
            if arr[i] > arr[i - 1]:  # Check if current is greater than the previous
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1  # Reset the count for a new subsequence
            i += 1  # Move to the next element

        return max_cnt


n = int(input())
sol = Solution()
ans = sol.max_inc(n)
print(ans)
