def first_last6(nums):
    '''Given an array of ints, return True if 6 appears as either the first or last element in the array.
    The array will be length 1 or more. '''
    end = len(nums)-1
    if nums[0] == 6 or nums[end] == 6:
        return True
    else:
        return False
