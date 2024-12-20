class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # Edge cases
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 0      # Number of jumps made
        curr_end = 0   # Farthest index reachable in the current jump
        farthest = 0    # Farthest index reachable overall
        curr_idx = 0    # Current index
        
        while curr_idx < n - 1:
            # Update the farthest index we can reach from current index
            farthest = max(farthest, curr_idx + arr[curr_idx])
            
            # If we have reached the end of our current jump range
            if curr_idx == curr_end:
                jumps += 1  # We need to make a jump
                curr_end = farthest  # Update the end for the next jump
                
                # If we can reach or exceed the last index
                if curr_end >= n - 1:
                    return jumps
            
            curr_idx += 1
            
            # If at any point we can't move forward
            if curr_idx > farthest:
                return -1
        
        return jumps



# Main program
while True:
    ip = input("Enter array elements (or type 'stop' to end): ").strip()

    if ip.lower() == "stop":
        break

    try:
        if " " in ip:
            # Space-separated numbers
            arr = list(map(int, ip.split()))
        else:
            # Single concatenated number
            arr = list(map(int, ip))
        
        sol = Solution()
        answer = sol.min_jumps(arr)
        print("Minimum jumps:", answer)
    except ValueError:
        print("Invalid input! Please enter valid numbers.")




