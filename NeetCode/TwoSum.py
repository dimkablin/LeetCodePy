class Solution(object):
    def twoSum(self, nums, target):
        hash_ = {}

        for i in range(len(nums)):
            hash_[nums[i]] = i

        for i in range(len(nums)):
            b = target - nums[i]
            if b in hash_ and hash_[b] != i:
                return [i, hash_[b]]


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        O(n^2)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]