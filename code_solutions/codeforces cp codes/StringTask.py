'''in the given string, consisting if uppercase and lowercase Latin letters, it:

deletes all the vowels,
inserts a character "." before each consonant,
replaces all uppercase consonants with corresponding lowercase ones.

Input
Codeforces

Output
.c.d.f.r.c.s'''

class Solution:
    def __init__(self):
        pass
    
    def string_task(self, word):
        new_word = []
        for w in word.lower():
            if w not in ['a','e','i','o','u','y']:
                new_word.append('.')
                new_word.append(w)
        print(''.join(new_word))


word = input().strip()
sol = Solution()
sol.string_task(word)

        
    