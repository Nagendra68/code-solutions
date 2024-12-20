class Solution:
    def easy_problem_search(self, vote):
        if 1 in vote:
            return "HARD"
        else:
            return "EASY"



n = int(input())
ip = input()
try:
    if " " in ip:
        # Space-separated numbers
        arr = list(map(int, ip.split()))
    else:
        # Single concatenated number
        arr = list(map(int, ip))
        
    sol = Solution()
    answer = sol.easy_problem_search(arr)
    print(answer)
except ValueError:
    print("Invalid input! Please enter valid numbers.")





