from typing import List

class Solution:
    def gcd(self, a: int, b: int) -> int:
        # Euclidean algorithm to find GCD
        while b:
            a, b = b, a % b
        return a

    def lcmAndGcd(self, a: int, b: int) -> List[int]:
        # Calculate GCD first
        gcd_value = self.gcd(a, b)
        # Calculate LCM using the formula
        lcm_value = (a * b) // gcd_value
        return [lcm_value, gcd_value]