"""
134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        offsets = []
        curMin = 10000
        curMin_idx = -1
        tmp = 0
        for i in range(len(gas)):
            offsets.append(gas[i]-cost[i])
            tmp += gas[i]-cost[i]
            if tmp < curMin:
                curMin_idx = i
                curMin = tmp
        if curMin_idx == len(gas)-1:
            start_idx = 0
        else:
            start_idx = curMin_idx + 1
        base = 0
        for i in list(range(start_idx, len(gas))) + list(range(0, start_idx)):
            base += offsets[i]
            if base < 0:
                return -1
            
        return start_idx

"""
Runtime: 636 ms, faster than 64.43% of Python online submissions for Gas Station.
Memory Usage: 23 MB, less than 17.24% of Python online submissions for Gas Station.
"""
