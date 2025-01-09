class Solution:
    def ATC(self):  
        # Number of test cases
        t = int(input())  
        final = []

        # Process each test case
        for _ in range(t):
            # Input: n (half the total number of students)
            n = int(input())
            # Input: skill levels of 2n students
            skills = list(map(int, input().split()))
            
            # Step 1: Sort the skill levels
            skills.sort()

            # Step 2: Find the minimum difference between the two middle elements
            # Median of the first class is skills[n - 1], median of the second class is skills[n]
            result = abs(skills[n] - skills[n - 1])
            
            # Output the result
            final.append(result)

        for i in final:
            print(i)

sol = Solution()
sol.ATC()