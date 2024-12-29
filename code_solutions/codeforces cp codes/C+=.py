def solve():
    t = int(input())  # Number of test cases
    results = []
    for _ in range(t):
        a, b, n = map(int, input().split())
        operations = 0
        while max(a, b) <= n:
            if a < b:
                a += b
            else:
                b += a
            operations += 1
        results.append(operations)
    
    # Print all results
    print("\n".join(map(str, results)))

# Example usage
solve()
