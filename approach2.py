def rotate(nums, k):
    n = len(nums)

    k = k % n

    nums.reverse()

    nums[:k] = reversed(nums[:k])

    nums[k:] = reversed(nums[k:])


# Input
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter number of rotations: "))

# Rotate the array
rotate(nums, k)

# Output
print("Rotated array:", nums)