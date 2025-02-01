def chocolates(n, nums):
    total = nums[-1]
    for i in range(n-2, -1, -1):
        if nums[i] >= nums[i+1]:
            nums[i] = max(0, nums[i+1]-1)
        total += nums[i]
    return total    


n = int(input())
nums = list(map(int, input().split()))

print(chocolates(n, nums))