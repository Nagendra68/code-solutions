t = int(input())  # Number of test cases
for _ in range(t):
    n = input()  # Read the number as a string to split easily
    round_numbers = []
    length = len(n)
    
    # Process each digit and form round numbers
    for i in range(length):
        if n[i] != '0':  # If digit is non-zero, form the round number
            round_numbers.append(n[i] + '0' * (length - i - 1))
    
    # Print the result
    print(len(round_numbers))  # Number of round numbers
    print(" ".join(round_numbers))



