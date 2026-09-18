def rotate(nums, k):
    n = len(nums)

    k = k % n

    for _ in range(k):
        last = nums[-1]

        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]

        nums[0] = last


# Input
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter number of rotations: "))

# Rotate the array
rotate(nums, k)

# Output
print("Rotated array:", nums)