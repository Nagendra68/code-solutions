class Solution:
    def min_dist2(self, digits2):
        sum_list = []
        current_sum = 0
        n = len(digits2)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    current_sum += abs(digits[i] - digits[j])
            sum_list.append(current_sum)
        return min(sum_list)



# Input: Space-separated digits (e.g., "1 2 3 4 5")
digits = list(map(int, input("Enter digits: ").strip().split()))
solution = Solution()
answer = solution.min_dist2(digits)
print("Minimum sum of absolute differences:", answer) 
