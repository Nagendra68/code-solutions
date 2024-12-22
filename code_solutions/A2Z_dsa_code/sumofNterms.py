
class Solution:
    def sumOfSeries(self,n):
        #code here
        if n == 1:
            return n
        return self.sumOfSeries(n-1)+(n**3)
