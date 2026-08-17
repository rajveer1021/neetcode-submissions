class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):

            # Skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1
            R = len(nums) - 1

            while L < R:

                current = nums[i] + nums[L] + nums[R]

                if current == 0:

                    result.append([nums[i], nums[L], nums[R]])

                    L += 1
                    R -= 1

                    # Skip duplicate L
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

                    # Skip duplicate R
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

                elif current < 0:
                    L += 1

                else:
                    R -= 1

        return result