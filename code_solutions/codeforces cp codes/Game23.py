def number_of_moves(n, m):
    if m % n != 0:
        return -1
    factor = m // n
    count = 0
    while factor % 2 ==0:
        factor //=2
        count += 1
    while factor % 3 == 0:
        factor //= 3
        count += 1

    if factor != 1:
        return -1
    
    return count

        

n,m = map(int,input().split())
print(number_of_moves(n,m))
