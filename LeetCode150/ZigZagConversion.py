class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = ""
        le = (numRows - 1) * 2

        for j in range(0, numRows):
            for i, sym in enumerate(s):
                if i % le == j or i % le == le-j:
                    result += sym

        return result


if __name__ == "__main__":
    solution = Solution()
    res = solution.convert("0123456789", 4)
    print(res)

