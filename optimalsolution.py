def rotate(nums, k):
    n = len(nums)
    k = k % n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


# Input
nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter number of rotations: "))

# Rotate the array
rotate(nums, k)

# Output
print("Rotated array:", nums)