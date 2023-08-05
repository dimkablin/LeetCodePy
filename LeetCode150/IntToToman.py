class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000: "M",
                 500: "D",
                 100: "C",
                 50: "L",
                 10: "X",
                 9: "IX",
                 5: "V",
                 4: "IV",
                 1: "I"
                 }

        result = ""

        #while num != 0:


