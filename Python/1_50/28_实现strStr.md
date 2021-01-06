# [实现strStr()](https://leetcode-cn.com/problems/implement-strstr/submissions/)

## 描述  
**简单** 
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

**示例1：** 

    输入: haystack = "hello", needle = "ll"
    输出: 2

**示例2：**


    输入: haystack = "aaaaa", needle = "bba"
    输出: -1

## 解题  

这个题，嗯，KMP，简单吗？  

然后就投机取巧了，哈哈

以后再补

```python 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```