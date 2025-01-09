import math

class Solution:
    def numbers_on_whiteboard(self):
        t = int(input())
        results = []

        for _ in range(t):
            n = int(input())

            # Output the minimum possible number left
            results.append(str(2))

            # Generate the sequence of pairs
            pairs = []
            for i in range(n, 1, -1):
                pairs.append((i, i - 1))

            # Append pairs to the results
            results.extend(f"{a} {b}" for a, b in pairs)

        # Print all results
        print("\n".join(results))

# Example usage
sol = Solution()
sol.numbers_on_whiteboard()





