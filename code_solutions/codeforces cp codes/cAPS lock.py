def process_word(word):
    # Check if all characters are uppercase
    if word.isupper():
        return word.lower()
    
    # Check if only the first character is lowercase and rest are uppercase
    if len(word) > 1 and word[0].islower() and word[1:].isupper():
        return word.capitalize()  # Capitalize changes first letter to uppercase and others to lowercase
    
    return word

# Input reading
input_word = input().strip()
result = process_word(input_word)
print(result)


