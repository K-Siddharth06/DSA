class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        if costBoth >= cost1 + cost2:
            return need1 * cost1 + need2 * cost2

        common = min(need1, need2)
        remaining = max(need1, need2) - common

        return common * costBoth + remaining * min(costBoth, cost1 if need1 > need2 else cost2)