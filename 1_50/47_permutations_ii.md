# [全排列II](https://leetcode-cn.com/problems/permutations-ii/)

## 描述  
**中等** 
给定一个可包含重复数字的序列，返回所有不重复的全排列。

## 示例

    输入: [1,1,2]
    输出:
    [
        [1,1,2],
        [1,2,1],
        [2,1,1]
    ]

## 解题  
在46题的基础上添加去重的语句，并事先需要将数字排序，以便在回溯中去重  

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def back(nums, temp):
            if not nums:
                res.append(temp)
                return 
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                back(nums[:i]+nums[i+1:], temp+[nums[i]])
        
        back(nums, [])
        return res
```