class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max = right_max = res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res
    
def main():
    # 测试用例1：经典示例
    test1 = [4,2,0,3,2,5]
    print(f"测试用例1结果: {Solution().trap(test1)}")  # 预期输出6
    
    # 测试用例2：无凹陷
    test2 = [4,3,2,1]
    print(f"测试用例2结果: {Solution().trap(test2)}")  # 预期输出0
    
    # 测试用例3：单凹陷
    test3 = [2,0,2]
    print(f"测试用例3结果: {Solution().trap(test3)}")  # 预期输出2

if __name__ == "__main__":
    main()