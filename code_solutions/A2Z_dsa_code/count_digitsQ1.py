class Solution:
    def evenlyDivides(self, n):
        p = str(n)
        cnt = 0
        for i in p:
            i = int(i)
            if i!=0:
                if n%i == 0:
                    cnt+=1
        return cnt
        
        