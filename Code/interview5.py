def find_duplicates(nums):
    n = len(nums)
    for i in range(n):
        index = abs(nums[i]) % n
        if nums[index] >= 0:
            nums[index] = -nums[index]
        else:
            print(f"Duplicate found: {abs(nums[i])}")

nums = [1, 2, 3, 1, 5]
find_duplicates(nums)
