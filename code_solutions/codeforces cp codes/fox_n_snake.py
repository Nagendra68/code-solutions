# class Solution:
#     def fox_n_snake(self, n, m):
#         for i in range(n):  # Loop through each row
#             if i % 2 == 0:  # Full row of '#'
#                 print("#" * m)
#             elif i % 4 == 1:  # Row where '#' is at the end
#                 print("." * (m - 1) + "#")
#             else:  # Row where '#' is at the start
#                 print("#" + "." * (m - 1))

# # Example Usage:
# n, m = map(int, input().split())  # Input dimensions n and m
# sol = Solution()
# sol.fox_n_snake(n, m)

# n, m = map(int, input().split())  # Input dimensions n and m

# for i in range(n):  # Loop through rows
#     if i % 2 == 0:  # Full row of '#'
#         print("#" * m)
#     elif i % 4 == 1:  # Row where '#' is at the end
#         print("." * (m - 1) + "#")
#     else:  # Row where '#' is at the start
#         print("#" + "." * (m - 1))

import sys

input = sys.stdin.read  # Ensures proper input handling for Codeforces

def fox_and_snake():
    n, m = map(int, input().split())  # Input dimensions n (rows) and m (columns)
    
    for i in range(n):
        if i % 2 == 0:  # Full row of '#'
            print("#" * m)
        elif i % 4 == 1:  # Row where '#' is at the end
            print("." * (m - 1) + "#")
        elif i % 4 == 3:  # Row where '#' is at the start
            print("#" + "." * (m - 1))

fox_and_snake()








                    

        





t = list(map(int,input().strip().split()))


