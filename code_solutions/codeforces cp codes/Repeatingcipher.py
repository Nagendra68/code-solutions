# 10
# ooopppssss

class Answer:
    def __init__(self):
        pass

    def decrypt_repeating_cipher(self,n, t):
        s = []  # To store the decrypted string
        index = 0  # Start from the first character
        step = 1  # Step size for triangular skipping

        while index < n:
            s.append(t[index])  # Append the character at the current index
            index += step  # Move to the next index based on the current step
            step += 1  # Increment the step size

        print(''.join(s))  # Convert list to string and output

# Input
n = int(input("Enter the length of the encrypted string: "))
t = input("Enter the encrypted string: ").strip()

# Solve
sol = Answer()
sol.decrypt_repeating_cipher(n, t)



