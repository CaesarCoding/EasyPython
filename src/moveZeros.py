from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        
        for k in range(i, len(nums)):
            nums[k] = 0


if __name__ == "__main__":
    # 测试示例1
    nums1 = [0, 1, 0, 3, 12]
    print("示例1 输入:", nums1)
    sol = Solution()
    sol.moveZeroes(nums1)
    print("示例1 输出:", nums1)  # 预期输出: [1, 3, 12, 0, 0]