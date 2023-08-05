class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        temp = ""
        for i in range(len(strs[0])):
            temp = strs[0][i]
            for word in strs:
                if len(word) == i or temp != word[i]:
                    return result
            result += temp

        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.longestCommonPrefix(["flower", "flow", "flight"])

    print(result)