class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = 0
        for i in range(len(haystack)):
            if needle[k] == haystack[i]:
                k += 1
            else:
                k = 0

            if k == len(needle)-1:
                return i-k

        return -1