"""To solve the problem, you need to ensure that each character in the string
can be evenly divided into `k` parts. If any character's count is not divisible by `k`, 
it's impossible to form the required string, and you should return `-1`. If all characters' 
counts are divisible by `k`, construct a substring by repeating each character `count[char] // k` 
times and then repeat this substring `k` times to form the final string. """

def construct_string(s,k):
    cnt = {}
    for char in s:
        cnt[char] = cnt.get(char,0) + 1
    for char in cnt:
        if cnt[char] % k != 0:
            return -1
    result = ""
    for char in cnt:
        result += char * (cnt[char] // k)
    return result * k

k = int(input())
s = input()
print(construct_string(s,k))


