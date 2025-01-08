def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Number of students halved
        a = list(map(int, input().split()))  # Skill levels of students
        
        a.sort()  # Sort the skill levels
        
        # The minimum possible absolute difference is between the n-th and (n-1)-th element
        print(abs(a[n] - a[n-1]))

solve()
