class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in result:
                return [result[complement], i]
            result[num] = i
            
        