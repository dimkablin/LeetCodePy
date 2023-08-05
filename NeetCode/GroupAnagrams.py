from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word] = [word]

        return list(groups.values())


if __name__ == "__main__":
    solution = Solution()
    result = solution.groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    )

    print(result)
