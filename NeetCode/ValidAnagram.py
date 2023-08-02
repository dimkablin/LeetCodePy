from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(i for i in s)
        t = sorted(i for i in t)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True

    def isAnagram2(selfself, s, t):
        return sorted(s) == sorted(t)

    def isAnagram3(self, s, t):
        count = defaultdict(int)
        for i in s:
            count[i] += 1

        for i in t:
            count[i] -= 1

        for val in count.values():
            if val != 0:
                return False

        return True