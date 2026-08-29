class Solution:
    def shipWithinDays(self, weights, days):

        low = max(weights)
        high = sum(weights)

        while low < high:

            mid = (low + high) // 2

            if canShip(weights, days, mid):
                high = mid
            else:
                low = mid + 1

        return low


def canShip(weights, days, capacity):

    days_needed = 1
    current = 0

    for weight in weights:

        if current + weight <= capacity:
            current += weight
        else:
            days_needed += 1
            current = weight

    return days_needed <= days
        