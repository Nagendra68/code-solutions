# def max_occurrence_count(s):
#     from collections import Counter  # Import Counter to count characters

#     freq = Counter(s)  # Get character frequencies
#     return max(freq.values())  # Return the maximum frequency

def max_occurrence_count(s):
    freq = {}  # Dictionary to store character frequencies

    # Count occurrences of each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Find the maximum count
    max_count = 0
    for count in freq.values():
        if count > max_count:
            max_count = count

    return max_count


# Example usage
s = input()
print(max_occurrence_count(s))
