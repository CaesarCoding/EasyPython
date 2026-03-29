from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            value = nums[i]
            pos = map.get(target - value)
            if pos is not None:
                return [pos, i]
            else:
                map[value] = i

        return []
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1] since nums[0] + nums[1] == 9
