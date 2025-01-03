# InputCopy
# 3
# 010011
# 0
# 1111000
# OutputCopy
# 2
# 0
# 0
# Note

class Solution:
    def __init__(self):
        pass
    def Erasing_zero(self, n):
        results = []

        for _ in range(n):
            s = input().strip()
            
            # Find the first and last occurrence of '1'
            first_one = s.find('1')
            last_one = s.rfind('1')
            
            if first_one == -1:  # No '1' in the string
                results.append(0)
            else:
                # Count '0's between the first and last '1'
                zeros_to_remove = s[first_one:last_one + 1].count('0')
                results.append(zeros_to_remove)

        # Output all results
        print("\n".join(map(str, results)))


n = int(input())
sol = Solution()
sol.Erasing_zero(n)