class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

# Example usage:
sol = Solution()
n = int(input("Enter n: "))
print(sol.fib(n))
