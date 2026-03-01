from typing import List

class Solution:
    def __BinarySearch(self, nums: List[int], target: int) -> List[int]:
        p, q = len(nums), -1
        while q + 1 < p:
            x = (p + q) // 2
            if nums[x] < target:
                q = x
            else:
                p = x
        return p
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        给你一个按照非递减顺序排列的整数数组 nums,和一个目标值 target。
        请你找出给定目标值在数组中的开始位置和结束位置。
        如果数组中不存在目标值 target,返回 [-1, -1]。
        你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

        示例:

            输入:nums = [5,7,7,8,8,10], target = 8
            输出:[3,4]
        '''
        a = self.__BinarySearch(nums=nums, target=target)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        b = self.__BinarySearch(nums=nums, target=target + 1) - 1
        return [a, b]

    def findPeakElement(self, nums: List[int]) -> int:
        '''
        峰值元素是指其值严格大于左右相邻值的元素。
        给你一个整数数组 nums,找到峰值元素并返回其索引。
        数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
        你可以假设 nums[-1] = nums[n] = -∞ 。
        你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

        示例:
            输入:nums = [1,2,3,1]
            输出:2
        '''
        p = -1
        q = len(nums) - 1
        while p + 1 < q:
            x = (p + q) // 2
            if nums[x] < nums[x + 1]:
                p = x
            else:
                q = x
        return q
    
    def findMin(self, nums: List[int]) -> int:
        '''
        已知一个长度为 n 的数组，预先按照升序排列，
        经由 1 到 n 次 旋转 后，得到输入数组。
        例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
        若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
        若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
        注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 
        旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
        给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，
        并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
        你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

        示例:
            输入:nums = [3,4,5,1,2]
            输出:1
        '''
        p = -1
        q = len(nums) - 1
        while p + 1 < q:
            x = (p + q) // 2
            if nums[x] < nums[-1]:
                q = x
            else:
                p = x
        return nums[q]
    
    def search(self, nums: List[int], target: int) -> int:
        '''
        整数数组 nums 按升序排列，数组中的值 互不相同.在传递给函数之前,
        nums 在预先未知的某个下标 k(0 <= k < nums.length)上进行了向左旋转，
        使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1],
        ..., nums[k-1]]（下标 从 0 开始 计数）。
        例如[0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。
        给你旋转后的数组nums和一个整数 target,如果nums中存在这个目标值target,
        则返回它的下标,否则返回 -1 。
        你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

        示例:
            输入:nums = [4,5,6,7,0,1,2], target = 0
            输出:4
        '''
        def cheak(i: int) -> bool:
            if nums[i] > nums[-1]:
                return target > nums[-1] and nums[i] >= target
            else:
                return target > nums[-1] or nums[i] >= target
        
        p = -1
        q = len(nums)
        while p + 1 < q:
            x = (q + p) // 2
            if cheak(x):
                q = x
            else:
                p = x
        if q == len(nums) or nums[q] != target:
            return -1
        return q


if __name__ == '__main__':
    solution = Solution()
    print(solution.search(nums = [4,5,6,7,0,1,2], target = 0))
    