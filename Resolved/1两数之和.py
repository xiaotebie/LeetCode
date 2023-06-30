from typing import List

"""
我的解法：

两个循环分别遍历整个List，一个正序遍历，一个倒序遍历，下标相同的跳过，当符合要求：有两数之和等于target时将下标添加到relist中
这个算法的
时间复杂度为O(n^2)
空间复杂度为O(1)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        relist = []
        # 第一个数字的索引
        for num1index, num1 in enumerate(nums):
            for num2index, num2 in enumerate(nums):
                sum = num1 + num2
                if num1index != num2index:
                    if sum == target:
                        relist.append(num1index)
                        relist.append(num2index)
                        return relist


"""
leetcode解法

由于需要找出nums中的两个数
num1 + num2 = target
所以有:
target - num1 = num2

核心逻辑：
当target - num1的差值不在哈希表中，将num1的值和序号添加到哈希表中
直到：
target - num1的值能在哈希表中查到
则
target - num1的值也就是num2提前于num1出现在整个list中
所以返回的下标为：[hashtable[target - num], i]  i就是等式target - num1 = num2成立时的num1的下标
如果哈希表中未找到则返回空哈希表

所以只需要遍历一次，在找到第一个数num1的同时，在哈希表中找到对应的第二个值num2
"""


class Solution1:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


# 创建 Solution 类的实例对象
solution = Solution1()

# 准备测试用例
nums = [3, 3]
target = 6

# 调用 twoSum 方法获取返回结果
result = solution.twoSum1(nums, target)

# 打印返回结果
print(result)
