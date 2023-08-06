from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            for i in range(len(word)+1):
                if i == len(word):
                    prefix = prefix[:i]

                if i+1 > len(prefix):
                    break

                if prefix[i] != word[i]:
                    prefix = prefix[:i]


        return prefix


if __name__ == "__main__":
    solution = Solution()
    result = solution.longestCommonPrefix(["ab", "a"])

    print(result)