# def present_from_lena(n):
#     for i in range(n+1):
#         for j in range(n-i):
#             print(" ", end = " ")
#         for j in range(i+1):
#             print(j, end = " ")
#         for j in range(i-1, -1, -1):
#             print(j, end = " ")
#         print(end = "\n")

#     for i in range(n):
#         for j in range(i+1):
#             print(" ", end = " ")
#         for j in range(n-i):
#             print (j , end = " ")
#         for j in range(n-i-2, -1, -1):
#             print(j, end = " ")
#         print(end = "\n")

# n = int(input())
# present_from_lena(n)

def generate_handkerchief(n):
    # Total number of rows in the rhombus
    total_rows = 2 * n + 1
    
    # List to hold all lines of output
    lines = []
    
    # Generate top half including the middle row
    for i in range(n + 1):
        # Leading spaces
        spaces = ' ' * (2 * (n - i))
        
        # Increasing sequence
        increasing_numbers = list(range(i + 1))
        
        # Decreasing sequence
        decreasing_numbers = list(range(i - 1, -1, -1))
        
        # Combine both sequences
        line_numbers = increasing_numbers + decreasing_numbers
        
        # Create line string with space-separated numbers
        line_str = spaces + ' '.join(map(str, line_numbers))
        
        # Append to lines list
        lines.append(line_str)
    
    # Generate bottom half by reversing top half excluding middle row
    for i in range(n - 1, -1, -1):
        lines.append(lines[i])
    
    # Print all lines
    for line in lines:
        print(line)

# Input reading
n = int(input().strip())
generate_handkerchief(n)

