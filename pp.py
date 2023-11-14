def remove_duplicates(nums):
    if not nums:
        return 0

    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1

    return j
nums = [1, 1, 2, 3]
result_length = remove_duplicates(nums)
print(result_length)