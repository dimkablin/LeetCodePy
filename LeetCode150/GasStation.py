class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start_station = 0
        cur_gas = 0
        total_gas = 0

        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]

            if cur_gas < 0:
                cur_gas = 0
                start_station = i + 1

        return start_station if total_gas >= 0 else -1


if __name__ == "__main__":
    solution = Solution()
    n = solution.canCompleteCircuit(
        gas=[5,1,2,3,4],
        cost=[4,4,1,5,1]
    )
    print(n)