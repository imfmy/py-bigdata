from typing import List


# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
# 可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # 使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 O(N)O(N)O(N) 降低到 O(1)O(1)O(1)。
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


# 创建 Solution 实例
solution = Solution()
if __name__ == '__main__':
    # 示例输入
    nums = [2, 7, 11, 15]
    target = 9

    # 调用 twoSum 方法
    result = solution.twoSum(nums, target)
    result1 = solution.twoSum1(nums, target)
    # 打印结果
    print(result)  # 输出 [0, 1]
    print(result1)
    print(enumerate(nums))
