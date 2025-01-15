'''input 
4
5 10 4
4 5 20
2 2 3
1000000000 1000000000 1000000000
output
-1 20
8 -1
1 2
-1 1000000000
'''
t = int(input())
results = []

def donut_shops(a, b, c):
    if a < c:
        first_shop = 1
    else:
        first_shop = -1

    if a * b > c:
        second_shop = b
    else:
        second_shop = -1

    return first_shop, second_shop

for i in range(t):
    a, b, c = map(int, input().split())
    result = donut_shops(a, b, c)
    results.append(result)

for res in results:
    print(res[0], res[1])



