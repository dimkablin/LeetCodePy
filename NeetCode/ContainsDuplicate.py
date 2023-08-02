class Solution(object):
    def containsDuplicate_1(self, nums) -> bool:
        """
        :type nums: List[int]
        :rtype: bool

        time: O(nlogn)
        space: O(1)
        """

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

    def containsDuplicates_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        time: O(n)
        space: O(n)
        """

        seen = list()

        for num in nums:
            if num in seen:
                return True
            seen.append(num)

        return False


