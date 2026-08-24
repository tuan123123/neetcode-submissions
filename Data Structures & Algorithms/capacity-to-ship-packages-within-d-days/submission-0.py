class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def ship(capacity):
            days_needed = 1
            current = 0

            for weight in weights:
                if current + weight > capacity:
                    days_needed += 1
                    current = 0
            
                current += weight

            return days_needed <= days
    
        while left < right:
            mid = (left + right) // 2
            if ship(mid):
                right = mid
            else:
                left = mid + 1

        return left