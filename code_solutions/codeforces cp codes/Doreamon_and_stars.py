def min_steps(n, m):
    # Minimum number of moves (as many 2-steps as possible)
    min_moves = (n + 1) // 2  # Equivalent to math.ceil(n / 2)
    
    # Find the smallest number >= min_moves that is a multiple of m
    if min_moves % m != 0:
        min_moves = ((min_moves // m) + 1) * m
    
    # If min_moves exceeds n, it's impossible
    if min_moves > n:
        return -1
    
    return min_moves

# Input
n, m = map(int, input().split())
result = min_steps(n, m)
print(result)
