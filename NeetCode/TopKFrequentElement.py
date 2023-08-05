from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_list = defaultdict(int)

        for num in nums:
            top_list[num] += 1

        freq_array = [[] for i in range(len(nums) + 1)]
        for num, freq in top_list.items():
            freq_array[freq].append(num)

        result = []
        for i in range(len(freq_array) - 1, -1, -1):
            for n in freq_array[i]:
                result.append(n)
                if len(result) == k:
                    return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.topKFrequent(
        [-1, 2],
        k=2
    )

    print(result)


