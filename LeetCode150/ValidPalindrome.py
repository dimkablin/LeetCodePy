class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        s = s.lower()

        while i < j:
            if not s[i].isalpha() and not s[i].isdigit():
                i += 1
                continue
            if not s[j].isalpha() and not s[j].isdigit():
                j -= 1
                continue

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":

    solution = Solution()
    res = solution.isPalindrome("0P")
    print(res)