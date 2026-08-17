class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        suffix = []
        result = []
        product = 1

        for i in range(len(nums)-1, -1, -1):
            if i+1 == len(nums):
                suffix.append(product)
            else:
                suffix.append(product * nums[i+1])
                product = product * nums[i+1]


        for i in range(0, len(nums)):
            if i == 0:
                product = 1
                result.append(product*suffix[len(nums)-i-1])
            else:
                product = product * nums[i-1]
                result.append(product*suffix[len(nums)-i-1])
                
        return result

            


        