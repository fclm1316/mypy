# encoding:utf-8
# File: 0001.py
# Author:fbi
# Time: 20/11/12
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
import time
def townum(nums, target):
    """
    枚举字典化列表,通过不变的target 减去 nums 来判断是否是字典中的key
    nums 不能有重复值
    :param nums:
    :param target:
    :return:
    """
    dic = {}
    for i, num in enumerate(nums):
        dic[num] = i
        if target - num in dic:
            print([dic[target - num], i])


if __name__ == '__main__':
    start_time = time.time()
    nums = [0, 2, 7, 11, 15, 16, 20, 34, 50, 32, 55, 66]
    target = 66
    townum(nums, target)
    print(time.time() - start_time)
