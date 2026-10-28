class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        answer = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer