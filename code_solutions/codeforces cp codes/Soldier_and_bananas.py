'''Input
3 17 4 cost of the first banana, 
initial number of dollars 
the soldier has 
and number of bananas he wants
Output
13'''
class Solution():
    def Soldier_n_Bananas(self, statement):    
        price = total = 0
        for i in range(1,statement[-1]+1):
            price = price+ statement[0]*i

        total = statement[1] - price
        if total>0:
            print(0)
        else:
            print(abs(total))


statement = list(map(int,input().split()))
sol = Solution()
sol.Soldier_n_Bananas(statement)


