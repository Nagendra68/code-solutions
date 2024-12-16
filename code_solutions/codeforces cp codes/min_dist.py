class Solution:
    def min_dist(self, digits):
        sum_list = []
        for i in range(len(digits)):
            current_sum = 0  # Initialize sum for each index
            for j in range(i + 1, len(digits)):
                current_sum += abs(digits[i] - digits[j])
            sum_list.append(current_sum)
        return min(sum_list)

    # def min_dist2(self, digits2):
    #     sum_list = []
    #     n = len(digits2)
    #     for i in range(n):
    #         for j in range(n):
    #             if i!=j:
    #                 current_sum += abs(digits[i] - digits[j])
    #         sum_list.append(current_sum)
    #     return min(sum_list)



# Input: Space-separated digits (e.g., "1 2 3 4 5")
digits = list(map(int, input("Enter digits: ").strip().split()))
solution = Solution()
answer = solution.min_dist(digits)
print("Minimum sum of absolute differences:", answer) 
