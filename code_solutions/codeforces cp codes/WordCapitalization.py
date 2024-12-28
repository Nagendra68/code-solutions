# Input
# ApPLe
# Output
# ApPLe
# Input
# konjac
# Output
# Konjac


class Solution:
    def wordCapitalization(self, word):
        new_word = word[0].upper() + word[1:]
        return new_word


word = input()
sol = Solution()
ans = sol.wordCapitalization(word)
print(ans)