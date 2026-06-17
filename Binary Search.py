def search(nums: [int], target: int):
    # write your code logic !!
    count=-1
    for i in range(0,len(nums)):
        if target==nums[i]:
            count=i
    return count
