class Solution:
    def __init__(self):
        pass

    def fix_conveyor_belt(self, test_cases):
        results = []

        for case in test_cases:
            n, m, grid = case["n"], case["m"], case["grid"]
            changes = 0

            # Check the last column (must all be 'D' except (n, m))
            for i in range(n - 1):  # Skip the last row
                if grid[i][m - 1] != 'D':
                    changes += 1

            # Check the last row (must all be 'R' except (n, m))
            for j in range(m - 1):  # Skip the last column
                if grid[n - 1][j] != 'R':
                    changes += 1

            results.append(changes)

        return results


# Input Parsing
def parse_input():
    t = int(input())  # Number of test cases
    test_cases = []

    for _ in range(t):
        n, m = map(int, input().split())
        grid = [input().strip() for _ in range(n)]
        test_cases.append({"n": n, "m": m, "grid": grid})

    return test_cases


# Execution
sol = Solution()
test_cases = parse_input()
results = sol.fix_conveyor_belt(test_cases)

# Output Results
for res in results:
    print(res)


