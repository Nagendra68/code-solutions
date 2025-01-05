# 10
# ooopppssss

class Answer:
    def __init__(self):
        pass

    def decrypt_repeating_cipher(self,n, t):
        index = 0
        word = []
        step = 1
        while(index<n):
            word.append(t[index])
            index+=step
            step+=1

        print(''.join(word))


# Input
n = int(input())
t = input().strip()

# Solve
sol = Answer()
sol.decrypt_repeating_cipher(n, t)



