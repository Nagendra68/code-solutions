def solve():
    t = int(input())  # Number of test cases
    results = []
    
    for _ in range(t):
        n = int(input())
        
        # Store operations
        operations = []
        
        # Initial numbers on the board: 1 to n
        current = n
        for i in range(n - 1, 0, -1):
            operations.append((current, i))
            current = (current + i + 1) // 2  # Equivalent to math.ceil((current + i) / 2)
        
        # Add results to output
        results.append(str(current))
        results.extend(f"{a} {b}" for a, b in operations)
    
    # Print all results at once
    print("\n".join(results))

# Example usage
solve()




