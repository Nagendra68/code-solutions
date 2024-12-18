'''Tetrahedron. Tetrahedron has 4 triangular faces.
Cube. Cube has 6 square faces.
Octahedron. Octahedron has 8 triangular faces.
Dodecahedron. Dodecahedron has 12 pentagonal faces.
Icosahedron. Icosahedron has 20 triangular faces.

i/p ->
4
Icosahedron
Cube
Tetrahedron
Dodecahedron

o/p -> 42'''

class Solution:
    def Anton_and_Polyhedrons(Self, n):
        sum = 0
        for _ in range(n):
            shape = input()
            if shape == "Tetrahedron":
                sum += 4
            elif shape == "Cube":
                sum += 6
            elif shape == "Octahedron":
                sum += 8
            elif shape == "Dodecahedron":
                sum += 12
            elif shape == "Icosahedron":
                sum += 20

        return sum

n = int(input())
sol = Solution()
result = sol.Anton_and_Polyhedrons(n)
print(result)
