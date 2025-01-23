def main():
    s = input().strip()

    all_upper = True

    # Check if all characters except the first are uppercase
    for i in range(1, len(s)):
        if not s[i].isupper():
            all_upper = False
            break

    # If all characters except the first are uppercase or string size is 1
    if all_upper or len(s) == 1:
        s = s[0].swapcase() + s[1:].lower()

    print(s)

if __name__ == "__main__":
    main()

