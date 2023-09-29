def isMonotonic(nums):
    is_increasing = True
    is_decreasing = True
    for index in range(1, len(nums) - 1):
        if nums[index + 1] > nums[index]:
            if (nums[index - 1] >= nums[index + 1] or nums[index] < nums[index - 1]) or not is_increasing:
                return False
            is_decreasing = False
        elif nums[index + 1] < nums[index]:
            if (nums[index - 1] <= nums[index + 1] or nums[index] > nums[index - 1]) or not is_decreasing:
                return False
            is_increasing = False
    return True
