def main():
    s = input().strip()
 
    # If the string is a single character, convert it to lowercase if it's uppercase
    if len(s) == 1:
        if s.isupper():
            print(s.lower())
        else:
            print(s.upper())
        return 
    
    # Check if all characters except the first are uppercase
    all_upper = True
    for i in range(1, len(s)):
        if not s[i].isupper():
            all_upper = False
            break

    # If the string is already entirely in lowercase, keep it unchanged
    if s.islower():
        print(s)
        return
    
    # Check the conditions for transformation
    if all_upper or len(s) == 1:
        # If all characters except the first are uppercase or string size is 1
        s = s[0].swapcase() + s[1:].lower()
    elif s[0].islower() and all_upper:
        # If first character is lowercase and the rest are uppercase, swap the case
        s = s.swapcase()
 
    # Otherwise, keep the string unchanged
    print(s)
 
if __name__ == "__main__":
    main()

