def yes_or_no(a, n, t):
    i = 1
    while i < t:
        i += a[i - 1]
        if i == t:
            return "YES"
    return "NO"

n, t = map(int, input().split())
a = list(map(int,input().split()))
print(yes_or_no(a, n, t))

