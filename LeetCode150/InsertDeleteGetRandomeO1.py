import random


class RandomizedSet(object):

    def __init__(self):
        self.RandomizedSet = {}
        self.actual_array = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.RandomizedSet:
            return False

        self.RandomizedSet[val] = len(self.actual_array)
        self.actual_array.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val not in self.RandomizedSet:
            return False

        self.RandomizedSet.pop(val)
        self.actual_array.remove(val)
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.actual_array)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()