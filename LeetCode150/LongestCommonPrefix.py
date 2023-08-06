from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            i=0
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[:i]
        return prefix


if __name__ == "__main__":
    solution = Solution()
    result = solution.longestCommonPrefix(["ab", "a"])

    print(result)