# InputCopy
# AS
# 2H 4C TH JH AD
# OutputCopy
# YES
# InputCopy
# 2H
# 3D 4C AC KD AS
# OutputCopy
# NO
# InputCopy
# 4D
# AS AC AD AH 5H
# OutputCopy
# YES

class Solution:
    def __init__(self):
        pass
    def Card_game(self):
        on_table = input().strip()
        on_hand = input().split()
        

        for card in on_hand:
            if on_table[0] == card[0] or on_table[1] == card[1]:
                return 'YES'
        return 'NO'
                
            
sol = Solution()
ans = sol.Card_game()
print(ans)

        