class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        s = s.lower()

        while( i != j):
            if not s[i].isalpha():
                i += 1
                continue
            if not s[j].isalpha():
                j -= 1

            if s[i] != s[j]:
                print(i, s[i], j, s[j])
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    print(int("a"), int("z"))

    solution = Solution()
    res = solution.isPalindrome("A man, a plan, a canal: Panama")
    print(res)