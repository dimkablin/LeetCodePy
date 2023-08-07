from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        for i in range(1, len(nums)):
            result[i] = result[i-1]*nums[i-1]

        temp = 1
        for i in range(n-1, -1, -1):
            result[i] *= temp
            temp *= nums[i]

        return result