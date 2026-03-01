from typing import List
from collections import Counter

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        给定一个含有 n 个正整数的数组和一个正整数 target 。
        找出该数组中满足其总和大于等于 target 的长度最小的 
        子数组 [numsl, numsl+1, ..., numsr-1, numsr] 返回其长度。
        如果不存在符合条件的子数组，返回 0 。

        示例:
            输入:target = 7, nums = [2,3,1,2,4,3]
            输出:2
        '''
        n = len(nums)
        p, s = 0, 0
        a = n + 1
        for q, x in enumerate(nums):
            s += x
            while s >= target:
                a = min(a, q - p + 1)
                s -= nums[p]
                p += 1
        return a if a < n + 1 else 0
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        给你一个整数数组 nums 和一个整数 k 。
        请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。

        示例:
            输入:nums = [10,5,2,6], k = 100
            输出:8
        '''
        if k <= 1:
            return 0
        n = len(nums)
        p, a, s = 0, 0, 1
        for q, x in enumerate(nums):
            s *= x
            while s >= k:
                s /= nums[p]
                p += 1
            a += q - p + 1
        return a

    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
        注:字串是连续的，子序列是不一定连续的
        例 1:
            输入:s = "abcabcbb"
            输出:3 
        '''
        a, p = 0,0
        cnt = Counter()
        for q, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[p]] -= 1
                p += 1
            a = max(a, q - p + 1)
        return a

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s = "abcabcbb"))