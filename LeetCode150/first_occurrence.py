class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i + len(needle)]:
                return i

        return -1


if __name__ == "__main__":
    solution = Solution()
    result = solution.strStr("abc", "c")

    print(result)