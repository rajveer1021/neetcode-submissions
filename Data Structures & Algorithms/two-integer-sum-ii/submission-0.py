class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) -1 

        for i in range(0, len(numbers) -1):
            if numbers[pointer1] + numbers[pointer2] < target:
                pointer1 +=1
            elif numbers[pointer1] + numbers[pointer2] == target:
                return [pointer1+1, pointer2+1]
            else:
                pointer2 -=1

        