# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# 44ms
# def twoSum(nums,target):
#     indices = []
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             value = nums[i]+nums[j]
#             if value == target:
#                 indices.append(i)
#                 indices.append(j)
#     return indices
#
#
# print(twoSum([2,7,11,15],18))

# 32ms
def twoSumEfficient(nums, target):
    dict = {}
    for i, value in enumerate(nums):
        complement = target - value
        if value in dict:
            return [dict[value],i]
        dict[complement] = i


print(twoSumEfficient([2, 7, 11, 15], 9))
