from typing import List

class Solution:
    def twoSum(self, numbers:List[int], target:int)-> List[int]:
        '''
        给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  
        请你从数组中找出满足相加之和等于目标数 target 的两个数。
        如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

        以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
        你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

        你所设计的解决方案必须只使用常量级的额外空间。

        示例：
            输入:list = [2, 3, 4, 5, 6, 8],target = 9
            输出:[2, 5]
        '''
        p, q = 0, len(numbers)-1
        while True:
            if numbers[p] + numbers[q] > target:
                q -= 1
            elif numbers[p] + numbers[q] < target:
                p += 1
            else:
                break
        return [p + 1, q + 1]

    def threeSum(self, nums: List[int])-> list[List[int]]:
        '''
        给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k
        同时还满足 nums[i] + nums[j] + nums[k] == 0 。
        请你返回所有和为 0 且不重复的三元组。

        注意：答案中不可以包含重复的三元组。

        示例：
            输入:nums = [-1,0,1,2,-1,-4]
            输出:[[-1,-1,2],[-1,0,1]]
        '''
        a = []
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            while j < k:
                s = nums[i] + nums[k] + nums[j]
                if s > 0 :
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    a.append([nums[i], nums[k], nums[j]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return a

    def maxArea(self, height: List[int]) -> int:
        '''
        给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
        返回容器可以储存的最大水量。

        说明：
            你不能倾斜容器。

        示例：
            输入:[1,8,6,2,5,4,8,3,7]
            输出:49 
        '''
        a:int = 0
        p = 0
        q = len(height) - 1
        while p < q:
            area = (q - p) * min(height[q], height[p])
            a = max(a, area)
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
        return a

    def trap_1(self, height: List[int]) -> int:
        '''
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

        示例：
            输入:height = [0,1,0,2,1,0,1,3,2,1,2,1]
            输出:6
        '''
        n = len(height)
        right_max = [0] * n
        left_max = [0] * n

        right_max[0] = height[0]
        for i in range(1, n):
            right_max[i] = max(height[i], right_max[i - 1])

        left_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            left_max[i] = max(height[i], left_max[i + 1])

        a = 0
        for i,j,k in zip(height, right_max, left_max):
            a += min(j, k) - i

        print(left_max)
        print(right_max)

        return a
    
    def trap_2(self, height: List[int]) -> int:
        '''
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

        示例：
            输入:height = [0,1,0,2,1,0,1,3,2,1,2,1]
            输出:6
        '''
        n = len(height)
        p, q = 0, n - 1
        right_max, left_max, a = 0, 0, 0
        while p <= q:
            right_max = max(right_max, height[p])
            left_max = max(left_max, height[q])
            if right_max < left_max:
                a += right_max - height[p]
                p += 1
            else:
                a += left_max - height[q]
                q -= 1
        return a

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap_2(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
